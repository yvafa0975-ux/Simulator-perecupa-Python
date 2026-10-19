import json
import math
import random
import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
from pathlib import Path
from datetime import datetime

SAVE_FILE = Path(__file__).with_name("config.json")
DEFAULTS = {"moneybal": 1000.0, "robux_balance": 0.0, "golds_balance": 0.0,
            "gems_balance": 0.0, "shards_balance": 0.0, "TGStars_balance": 0.0}
ITEMS = {
    "Golds": ("golds_balance", "Золото Standoff 2", 2.0, 1.5, "2 Golds за 1 ₽"),
    "Robux": ("robux_balance", "Robux", 1.5, 1.5, "1,5 Robux за 1 ₽"),
    "Gems": ("gems_balance", "Gems", 1.5, 2.5, "1,5 Gems за 1 ₽"),
    "Shards": ("shards_balance", "Shards", 5.0, 6.1, "5 Shards за 1 ₽"),
    "TGStars": ("TGStars_balance", "TGStars", 2 / 1.39, 2.0, "2 Stars за 1,39 ₽"),
}
PROMOS = {"3.0": 3000.0}
BG, SIDEBAR, PANEL = "#101722", "#0b111b", "#182536"
PANEL2, BORDER, TEXT, MUTED = "#213249", "#30445d", "#edf4ff", "#9eafc5"
BLUE, GREEN, PURPLE, RED = "#1686f8", "#14b879", "#9c62f5", "#e74c65"


def fmt(n):
    n = round(float(n), 2)
    return f"{int(n):,}".replace(",", " ") if n.is_integer() else f"{n:,.2f}".replace(",", " ").replace(".", ",")


def load_data():
    d = DEFAULTS.copy()
    d.update({"redeemed_codes": [], "history": [], "last_daily_bonus": ""})
    try:
        saved = json.loads(SAVE_FILE.read_text(encoding="utf-8"))
        if isinstance(saved, dict):
            for k in DEFAULTS:
                v = saved.get(k, d[k])
                if isinstance(v, (int, float)) and not isinstance(v, bool) and math.isfinite(v) and v >= 0:
                    d[k] = float(v)
            if isinstance(saved.get("redeemed_codes"), list):
                d["redeemed_codes"] = [str(x).upper() for x in saved["redeemed_codes"]]
            if isinstance(saved.get("history"), list):
                d["history"] = saved["history"][-100:]
            if isinstance(saved.get("last_daily_bonus"), str):
                d["last_daily_bonus"] = saved["last_daily_bonus"]
            # Also accept the earlier version's transaction field.
            if not d["history"] and isinstance(saved.get("transactions"), list):
                d["history"] = saved["transactions"][-100:]
    except (OSError, ValueError, TypeError):
        pass
    return d


def save_data(d):
    tmp = SAVE_FILE.with_suffix(".tmp")
    tmp.write_text(json.dumps(d, ensure_ascii=False, indent=2), encoding="utf-8")
    tmp.replace(SAVE_FILE)


class Game:
    def __init__(self, root):
        self.root = root
        root.title("Симулятор Перекупа 3.0")
        root.geometry("1180x780")
        root.minsize(920, 650)
        root.configure(bg=BG)
        self.d = load_data()
        self.status = tk.StringVar(value="Добро пожаловать! Удачной торговли.")
        self.page = "Главная"
        self.setup_styles()
        self.build_shell()
        self.show("Главная")
        root.protocol("WM_DELETE_WINDOW", self.close)

    def setup_styles(self):
        s = ttk.Style()
        try: s.theme_use("clam")
        except tk.TclError: pass
        s.configure("TFrame", background=BG)
        s.configure("Panel.TFrame", background=PANEL)
        s.configure("TLabel", background=BG, foreground=TEXT, font=("Segoe UI", 10))
        s.configure("Panel.TLabel", background=PANEL, foreground=TEXT, font=("Segoe UI", 10))
        s.configure("Muted.TLabel", background=PANEL, foreground=MUTED, font=("Segoe UI", 9))
        s.configure("Title.TLabel", background=BG, foreground=TEXT, font=("Segoe UI", 22, "bold"))
        s.configure("TButton", background=PANEL2, foreground=TEXT, padding=8, font=("Segoe UI", 10, "bold"))
        s.map("TButton", background=[("active", "#365273")])
        for style, color in [("Blue.TButton", BLUE), ("Green.TButton", GREEN), ("Purple.TButton", PURPLE), ("Red.TButton", "#702b3a")]:
            s.configure(style, background=color, foreground="white", padding=8, font=("Segoe UI", 10, "bold"))
            s.map(style, background=[("active", color)])

    def build_shell(self):
        top = tk.Frame(self.root, bg="#090f18", height=88)
        top.pack(fill="x"); top.pack_propagate(False)
        brand = tk.Frame(top, bg="#090f18"); brand.pack(side="left", padx=22, pady=12)
        tk.Label(brand, text="СИМУЛЯТОР ПЕРЕКУПА", bg="#090f18", fg=TEXT, font=("Segoe UI", 19, "bold")).pack(anchor="w")
        tk.Label(brand, text="ПОКУПАЙ • ПРОДАВАЙ • ЗАРАБАТЫВАЙ  /  GLOBAL 3.0", bg="#090f18", fg="#4ca7ff", font=("Segoe UI", 9, "bold")).pack(anchor="w")
        self.money_top = tk.Label(top, text="", bg="#090f18", fg="#39e6a0", font=("Segoe UI", 18, "bold"))
        self.money_top.pack(side="right", padx=26)
        tk.Label(top, text="ТВОЙ БАЛАНС", bg="#090f18", fg=MUTED, font=("Segoe UI", 8, "bold")).pack(side="right")
        body = tk.Frame(self.root, bg=BG); body.pack(fill="both", expand=True)
        side = tk.Frame(body, bg=SIDEBAR, width=205); side.pack(side="left", fill="y"); side.pack_propagate(False)
        tk.Label(side, text="НАВИГАЦИЯ", bg=SIDEBAR, fg="#637994", font=("Segoe UI", 9, "bold")).pack(anchor="w", padx=20, pady=(22, 10))
        self.nav = {}
        for icon, page in [("⌂", "Главная"), ("▣", "Магазин"), ("⇄", "Продажа"), ("🎰", "Казино"),
                           ("◆", "Промокоды"), ("🎁", "Бонус дня"), ("★", "Достижения"), ("▥", "Статистика"), ("⚙", "Настройки")]:
            b = tk.Button(side, text=f"  {icon}   {page}", anchor="w", relief="flat", bd=0, padx=13, pady=11,
                          bg=SIDEBAR, fg="#c6d4e7", activebackground="#203a59", activeforeground="white",
                          font=("Segoe UI", 10, "bold"), cursor="hand2", command=lambda p=page: self.show(p))
            b.pack(fill="x", padx=9, pady=2); self.nav[page] = b
        tk.Frame(side, bg=BORDER, height=1).pack(fill="x", padx=18, pady=18)
        tk.Label(side, text="Локальное сохранение\nconfig.json", bg=SIDEBAR, fg="#637994", justify="left", font=("Segoe UI", 8)).pack(anchor="w", padx=20)
        right = tk.Frame(body, bg=BG); right.pack(side="left", fill="both", expand=True)
        self.content = tk.Frame(right, bg=BG); self.content.pack(fill="both", expand=True, padx=24, pady=22)
        foot = tk.Frame(right, bg="#090f18", height=32); foot.pack(fill="x", side="bottom"); foot.pack_propagate(False)
        tk.Label(foot, textvariable=self.status, bg="#090f18", fg=MUTED, anchor="w", font=("Segoe UI", 9)).pack(fill="both", padx=15)

    def header(self, title, subtitle):
        tk.Label(self.content, text=title, bg=BG, fg=TEXT, font=("Segoe UI", 23, "bold")).pack(anchor="w")
        tk.Label(self.content, text=subtitle, bg=BG, fg=MUTED, font=("Segoe UI", 10)).pack(anchor="w", pady=(4, 16))

    def card(self, parent, title, subtitle=""):
        f = tk.Frame(parent, bg=PANEL, highlightthickness=1, highlightbackground=BORDER)
        tk.Label(f, text=title, bg=PANEL, fg=TEXT, font=("Segoe UI", 12, "bold")).pack(anchor="w", padx=15, pady=(13, 0))
        if subtitle:
            tk.Label(f, text=subtitle, bg=PANEL, fg=MUTED, font=("Segoe UI", 9), wraplength=700, justify="left").pack(anchor="w", padx=15, pady=(4, 10))
        return f

    def refresh_top(self):
        self.money_top.configure(text=f"{fmt(self.d['moneybal'])} ₽")

    def save(self):
        try: save_data(self.d)
        except OSError as e: self.status.set(f"Ошибка сохранения: {e}")

    def record(self, text):
        self.d["history"].append({"time": datetime.now().strftime("%d.%m.%Y %H:%M"), "text": text})
        self.d["history"] = self.d["history"][-100:]
        self.save()

    def show(self, page):
        self.page = page
        for w in self.content.winfo_children(): w.destroy()
        for name, b in self.nav.items():
            b.configure(bg="#1d4168" if name == page else SIDEBAR, fg="white" if name == page else "#c6d4e7")
        getattr(self, "page_" + {"Главная":"home","Магазин":"shop","Продажа":"sell","Казино":"casino",
                "Промокоды":"promos","Бонус дня":"daily","Достижения":"achievements","Статистика":"stats","Настройки":"settings"}[page])()
        self.refresh_top()

    def page_home(self):
        self.header("Главная", "Твой рынок — твои решения. Следи за балансом и развивай запасы.")
        banner = tk.Frame(self.content, bg="#15395e", highlightbackground="#2879b9", highlightthickness=1)
        banner.pack(fill="x", pady=(0, 14))
        tk.Label(banner, text="С возвращением, перекуп!", bg="#15395e", fg="white", font=("Segoe UI", 18, "bold")).pack(anchor="w", padx=20, pady=(16, 4))
        tk.Label(banner, text="Покупай ресурсы, продавай с выгодой и проверяй новые промокоды.", bg="#15395e", fg="#c5ddf7", font=("Segoe UI", 10)).pack(anchor="w", padx=20)
        ttk.Button(banner, text="ОТКРЫТЬ МАГАЗИН  →", style="Blue.TButton", command=lambda: self.show("Магазин")).pack(anchor="w", padx=20, pady=14)
        box = self.card(self.content, "ТВОИ ЗАПАСЫ", "Все игровые валюты в одном месте")
        box.pack(fill="x", pady=(0, 14))
        grid = tk.Frame(box, bg=PANEL); grid.pack(fill="x", padx=12, pady=12)
        for i, (name, (key, title, *_)) in enumerate(ITEMS.items()):
            tile = tk.Frame(grid, bg=PANEL2, padx=10, pady=10); tile.grid(row=0, column=i, sticky="nsew", padx=3)
            tk.Label(tile, text=name, bg=PANEL2, fg="#78b9ff", font=("Segoe UI", 9, "bold")).pack(anchor="w")
            tk.Label(tile, text=fmt(self.d[key]), bg=PANEL2, fg=TEXT, font=("Segoe UI", 13, "bold")).pack(anchor="w", pady=(5, 0))
            grid.columnconfigure(i, weight=1)
        row = tk.Frame(self.content, bg=BG); row.pack(fill="x")
        a = self.card(row, "Промокод недели", "Введи код 3.0 на странице промокодов.")
        a.pack(side="left", fill="both", expand=True, padx=(0, 7))
        tk.Label(a, text="3.0   +3 000 ₽", bg=PANEL, fg="#b88aff", font=("Segoe UI", 19, "bold")).pack(anchor="w", padx=15, pady=(0, 12))
        ttk.Button(a, text="АКТИВИРОВАТЬ", style="Purple.TButton", command=lambda: self.show("Промокоды")).pack(anchor="w", padx=15, pady=(0, 14))
        b = self.card(row, "Быстрые действия", "Выбирай, что сделать дальше")
        b.pack(side="left", fill="both", expand=True, padx=(7, 0))
        for text, p in [("Продать ресурсы", "Продажа"), ("Сыграть в казино", "Казино"), ("Забрать бонус дня", "Бонус дня"), ("Посмотреть статистику", "Статистика")]:
            ttk.Button(b, text=text, command=lambda p=p: self.show(p)).pack(fill="x", padx=14, pady=4)

    def page_shop(self):
        self.header("Магазин", "Выбери ресурс и укажи сумму в игровых рублях.")
        for name, (key, title, rate, sell, buytext) in ITEMS.items():
            c = self.card(self.content, title, f"Курс: {buytext}    •    В запасе: {fmt(self.d[key])}")
            c.pack(fill="x", pady=5)
            ttk.Button(c, text="КУПИТЬ", style="Green.TButton", command=lambda n=name: self.buy(n)).pack(anchor="e", padx=15, pady=(0, 12))

    def page_sell(self):
        self.header("Продажа", "Продай часть запасов и получи игровые рубли.")
        for name, (key, title, rate, sell, buytext) in ITEMS.items():
            c = self.card(self.content, title, f"Курс продажи: {sell:g} ₽ за единицу    •    В запасе: {fmt(self.d[key])}")
            c.pack(fill="x", pady=5)
            ttk.Button(c, text="ПРОДАТЬ", style="Blue.TButton", command=lambda n=name: self.sell(n)).pack(anchor="e", padx=15, pady=(0, 12))

    def page_casino(self):
        self.header("Казино", "Мини-игра на удачу. Ставь только виртуальные игровые рубли.")
        c = self.card(self.content, "🎲 Угадай число", f"Текущий баланс: {fmt(self.d['moneybal'])} ₽")
        c.pack(fill="x")
        tk.Label(c, text="Выбери 1 или 2. При победе выплата составит 2× ставки, при проигрыше ставка теряется.", bg=PANEL, fg=MUTED, wraplength=650, justify="left").pack(anchor="w", padx=15, pady=12)
        ttk.Button(c, text="ИГРАТЬ", style="Purple.TButton", command=self.casino).pack(anchor="w", padx=15, pady=(0, 15))

    def page_promos(self):
        self.header("Промокоды", "Активируй код, чтобы получить игровой бонус. Каждый код работает один раз.")
        c = self.card(self.content, "◆  АКТИВАЦИЯ ПРОМОКОДА", "Первый промокод уже доступен.")
        c.pack(fill="x", pady=(0, 14))
        row = tk.Frame(c, bg=PANEL); row.pack(fill="x", padx=15, pady=(6, 14))
        self.promo_entry = ttk.Entry(row, font=("Segoe UI", 12))
        self.promo_entry.pack(side="left", fill="x", expand=True, ipady=6)
        self.promo_entry.bind("<Return>", lambda e: self.redeem())
        ttk.Button(row, text="АКТИВИРОВАТЬ", style="Purple.TButton", command=self.redeem).pack(side="left", padx=(9, 0))
        listing = self.card(self.content, "ДОСТУПНЫЕ ПРОМОКОДЫ", "Официальные коды и их награды")
        listing.pack(fill="x")
        for code, reward in PROMOS.items():
            used = code.upper() in self.d["redeemed_codes"]
            line = tk.Frame(listing, bg=PANEL2, padx=13, pady=12); line.pack(fill="x", padx=14, pady=6)
            tk.Label(line, text=code, bg=PANEL2, fg="#c39aff", font=("Segoe UI", 15, "bold")).pack(side="left")
            tk.Label(line, text=f"+{fmt(reward)} игровых рублей", bg=PANEL2, fg=TEXT, font=("Segoe UI", 10)).pack(side="left", padx=18)
            tk.Label(line, text="УЖЕ ИСПОЛЬЗОВАН" if used else "ДОСТУПЕН", bg=PANEL2, fg=GREEN if used else "#7be3b5", font=("Segoe UI", 8, "bold")).pack(side="right")

    def page_daily(self):
        self.header("Бонус дня", "Заходи каждый день и забирай игровые рубли.")
        c = self.card(self.content, "🎁 ЕЖЕДНЕВНАЯ НАГРАДА", "Награда: 500 игровых рублей. Получить её можно один раз в календарный день.")
        c.pack(fill="x", pady=(0, 14))
        last = self.d.get("last_daily_bonus", "")
        today = datetime.now().strftime("%Y-%m-%d")
        if last == today:
            tk.Label(c, text="Сегодня бонус уже забран. Загляни завтра!", bg=PANEL, fg="#7be3b5",
                     font=("Segoe UI", 12, "bold")).pack(anchor="w", padx=15, pady=(0, 12))
            ttk.Button(c, text="УЖЕ ПОЛУЧЕНО", state="disabled").pack(anchor="w", padx=15, pady=(0, 15))
        else:
            tk.Label(c, text="Доступно прямо сейчас: +500 ₽", bg=PANEL, fg="#7be3b5",
                     font=("Segoe UI", 15, "bold")).pack(anchor="w", padx=15, pady=(0, 12))
            ttk.Button(c, text="ЗАБРАТЬ БОНУС", style="Green.TButton",
                       command=self.claim_daily_bonus).pack(anchor="w", padx=15, pady=(0, 15))
        info = self.card(self.content, "КАК ЭТО РАБОТАЕТ", "Бонус сохраняется вместе с игрой. Перезапуск приложения не позволит забрать его второй раз в тот же день.")
        info.pack(fill="x")

    def claim_daily_bonus(self):
        today = datetime.now().strftime("%Y-%m-%d")
        if self.d.get("last_daily_bonus", "") == today:
            messagebox.showinfo("Бонус дня", "Сегодня ты уже забрал награду.", parent=self.root)
            self.show("Бонус дня")
            return
        self.d["moneybal"] = round(self.d["moneybal"] + 500, 2)
        self.d["last_daily_bonus"] = today
        self.record("Получен ежедневный бонус: +500 ₽")
        self.status.set("Ежедневный бонус получен: +500 ₽.")
        messagebox.showinfo("Готово!", "Ты получил 500 игровых рублей!", parent=self.root)
        self.show("Бонус дня")

    def page_achievements(self):
        self.header("Достижения", "Маленькие цели для твоего игрового аккаунта.")
        operations = self.d["history"]
        checks = [
            ("Первая сделка", "Совершить хотя бы одну операцию", bool(operations)),
            ("Промокодер", "Активировать код 3.0", "3.0" in self.d["redeemed_codes"]),
            ("Капиталист", "Накопить 5 000 ₽", self.d["moneybal"] >= 5000),
            ("Коллекционер", "Иметь не менее 1 единицы каждого ресурса", all(self.d[x[0]] >= 1 for x in ITEMS.values())),
        ]
        for title, desc, done in checks:
            c = self.card(self.content, ("✓  " if done else "○  ") + title, desc)
            c.pack(fill="x", pady=5)
            tk.Label(c, text="ВЫПОЛНЕНО" if done else "ЕЩЁ ВПЕРЕДИ", bg=PANEL, fg=GREEN if done else MUTED, font=("Segoe UI", 8, "bold")).pack(anchor="w", padx=15, pady=(0, 12))

    def page_stats(self):
        self.header("Статистика", "Сводка по балансу и недавним операциям.")
        c = self.card(self.content, "ОБЩАЯ СТАТИСТИКА")
        c.pack(fill="x", pady=(0, 12))
        total = sum(self.d[x[0]] for x in ITEMS.values())
        for label, value in [("Игровые рубли", fmt(self.d["moneybal"]) + " ₽"), ("Всего единиц ресурсов", fmt(total)), ("Операций", str(len(self.d["history"]))), ("Использовано промокодов", str(len(self.d["redeemed_codes"])))]:
            line = tk.Frame(c, bg=PANEL); line.pack(fill="x", padx=15, pady=6)
            tk.Label(line, text=label, bg=PANEL, fg=MUTED).pack(side="left")
            tk.Label(line, text=value, bg=PANEL, fg=TEXT, font=("Segoe UI", 10, "bold")).pack(side="right")
        hist = self.card(self.content, "ПОСЛЕДНИЕ ОПЕРАЦИИ")
        hist.pack(fill="both", expand=True)
        tree = ttk.Treeview(hist, columns=("time", "text"), show="headings", height=8)
        tree.heading("time", text="Время"); tree.heading("text", text="Операция")
        tree.column("time", width=145); tree.column("text", width=600)
        tree.pack(fill="both", expand=True, padx=12, pady=12)
        for item in reversed(self.d["history"][-25:]):
            tree.insert("", "end", values=(item.get("time", ""), item.get("text", "")))

    def page_settings(self):
        self.header("Настройки", "Сохранение игры и управление прогрессом.")
        c = self.card(self.content, "СОХРАНЕНИЕ", "Файл config.json находится рядом с программой.")
        c.pack(fill="x", pady=(0, 12))
        ttk.Button(c, text="СОХРАНИТЬ СЕЙЧАС", style="Blue.TButton", command=self.manual_save).pack(anchor="w", padx=15, pady=(5, 8))
        ttk.Button(c, text="СБРОСИТЬ ПРОГРЕСС", style="Red.TButton", command=self.reset).pack(anchor="w", padx=15, pady=(0, 14))
        about = self.card(self.content, "О ПРОЕКТЕ", "Симулятор Перекупа 3.0 • магазин • продажа • казино • промокоды • бонус дня • достижения • статистика")
        about.pack(fill="x")

    def amount(self, title, prompt, maximum):
        n = simpledialog.askfloat(title, prompt, parent=self.root, minvalue=0.01)
        if n is None: return None
        if not math.isfinite(n) or n <= 0:
            messagebox.showerror("Ошибка", "Введи число больше нуля.", parent=self.root); return None
        if n > maximum + 1e-9:
            messagebox.showerror("Недостаточно средств", f"Доступно: {fmt(maximum)}.", parent=self.root); return None
        return round(n, 2)

    def buy(self, name):
        key, title, rate, sell, _ = ITEMS[name]
        n = self.amount("Покупка", f"Сколько игровых рублей потратить? Баланс: {fmt(self.d['moneybal'])} ₽", self.d["moneybal"])
        if n is None: return
        got = round(n * rate, 2)
        self.d["moneybal"] = round(self.d["moneybal"] - n, 2)
        self.d[key] = round(self.d[key] + got, 2)
        self.record(f"Куплено {fmt(got)} {name} за {fmt(n)} ₽")
        self.status.set(f"Покупка выполнена: +{fmt(got)} {name}.")
        self.show(self.page)

    def sell(self, name):
        key, title, rate, sellrate, _ = ITEMS[name]
        if self.d[key] <= 0:
            messagebox.showinfo("Нет ресурсов", f"У тебя пока нет {title}.", parent=self.root); return
        n = self.amount("Продажа", f"Сколько продать? В запасе: {fmt(self.d[key])}", self.d[key])
        if n is None: return
        proceeds = round(n * sellrate, 2)
        self.d[key] = max(0, round(self.d[key] - n, 2))
        self.d["moneybal"] = round(self.d["moneybal"] + proceeds, 2)
        self.record(f"Продано {fmt(n)} {name} за {fmt(proceeds)} ₽")
        self.status.set(f"Продажа выполнена: +{fmt(proceeds)} ₽.")
        self.show(self.page)

    def casino(self):
        bet = self.amount("Ставка", f"Сколько поставить? Баланс: {fmt(self.d['moneybal'])} ₽", self.d["moneybal"])
        if bet is None: return
        guess = simpledialog.askinteger("Казино", "Выбери число 1 или 2:", parent=self.root, minvalue=1, maxvalue=2)
        if guess is None: return
        result = random.randint(1, 2)
        if guess == result:
            self.d["moneybal"] = round(self.d["moneybal"] + bet, 2)
            msg = f"Победа! Выпало {result}. Чистая прибыль: {fmt(bet)} ₽."
            messagebox.showinfo("Победа!", msg, parent=self.root)
        else:
            self.d["moneybal"] = round(self.d["moneybal"] - bet, 2)
            msg = f"Не повезло: выпало {result}. Потеряно {fmt(bet)} ₽."
            messagebox.showinfo("Результат", msg, parent=self.root)
        self.record(msg); self.status.set(msg); self.show("Казино")

    def redeem(self):
        code = self.promo_entry.get().strip().upper()
        if not code:
            messagebox.showwarning("Промокод", "Введи промокод.", parent=self.root); return
        if code not in PROMOS:
            messagebox.showerror("Промокод", "Такого промокода нет.", parent=self.root); return
        if code in self.d["redeemed_codes"]:
            messagebox.showinfo("Промокод", "Этот код уже активирован на этом сохранении.", parent=self.root); return
        reward = PROMOS[code]
        self.d["moneybal"] = round(self.d["moneybal"] + reward, 2)
        self.d["redeemed_codes"].append(code)
        self.record(f"Активирован промокод {code}: +{fmt(reward)} ₽")
        self.status.set(f"Промокод {code} активирован: +{fmt(reward)} ₽.")
        messagebox.showinfo("Готово!", f"Промокод {code} активирован!\nНачислено {fmt(reward)} игровых рублей.", parent=self.root)
        self.show("Промокоды")

    def manual_save(self):
        try:
            save_data(self.d); self.status.set("Игра сохранена в config.json.")
            messagebox.showinfo("Сохранение", "Прогресс сохранён.", parent=self.root)
        except OSError as e: messagebox.showerror("Ошибка сохранения", str(e), parent=self.root)

    def reset(self):
        if not messagebox.askyesno("Сброс", "Сбросить все балансы, историю и использованные промокоды?", parent=self.root): return
        self.d = DEFAULTS.copy(); self.d.update({"redeemed_codes": [], "history": [], "last_daily_bonus": ""})
        self.save(); self.status.set("Прогресс сброшен."); self.show("Главная")

    def close(self):
        try: save_data(self.d)
        except OSError as e:
            if not messagebox.askyesno("Ошибка сохранения", f"{e}\nВыйти без сохранения?", parent=self.root): return
        self.root.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    Game(root)
    root.mainloop()
