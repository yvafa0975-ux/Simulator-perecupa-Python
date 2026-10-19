import json
import math
import random
import tkinter as tk
import base64
import webbrowser
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
                           ("◆", "Промокоды"), ("🎁", "Бонус дня"), ("★", "Достижения"), ("▥", "Статистика"), ("⚙", "Настройки"), ("ⓘ", "О проекте")]:
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
                "Промокоды":"promos","Бонус дня":"daily","Достижения":"achievements","Статистика":"stats","Настройки":"settings","О проекте":"about"}[page])()
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

    def page_about(self):
        self.header("О проекте", "Информация о Симуляторе Перекупа 3.0 и ссылка на исходный код.")
        intro = self.card(self.content, "СИМУЛЯТОР ПЕРЕКУПА 3.0",
                          "Небольшая игра про покупку и продажу игровых ресурсов, управление балансом и развитие своего аккаунта.")
        intro.pack(fill="x", pady=(0, 14))
        tk.Label(intro, text="Весь исходный код имеется на GitHub.",
                 bg=PANEL, fg=TEXT, font=("Segoe UI", 13, "bold")).pack(anchor="w", padx=15, pady=(5, 14))

        repo_url = "https://github.com/yvafa0975-ux/Simulator-perecupa-Python"
        link_area = tk.Frame(intro, bg=PANEL)
        link_area.pack(anchor="w", padx=15, pady=(0, 16))

        # Оригинальный логотип GitHub; внешний белый фон удалён.
        logo_data = "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"
        self.github_logo_image = tk.PhotoImage(data=logo_data).subsample(3, 3)
        logo = tk.Label(link_area, image=self.github_logo_image, bg=PANEL,
                        cursor="hand2", bd=0)
        logo.pack(side="left")
        logo.bind("<Button-1>", lambda _event: webbrowser.open_new_tab(repo_url))

        link_button = tk.Button(link_area, text="  Открыть репозиторий на GitHub  ↗",
                                command=lambda: webbrowser.open_new_tab(repo_url),
                                bg="#238636", fg="white", activebackground="#2ea043",
                                activeforeground="white", relief="flat", bd=0,
                                padx=14, pady=12, font=("Segoe UI", 10, "bold"),
                                cursor="hand2")
        link_button.pack(side="left", padx=(12, 0))
        tk.Label(intro, text=repo_url, bg=PANEL, fg="#78b9ff",
                 font=("Segoe UI", 9), cursor="hand2").pack(anchor="w", padx=15, pady=(0, 14))
        # Make the visible repository address clickable as well.
        for widget in intro.winfo_children():
            if isinstance(widget, tk.Label) and widget.cget("text") == repo_url:
                widget.bind("<Button-1>", lambda _event: webbrowser.open_new_tab(repo_url))

        details = self.card(self.content, "ЧТО ЕСТЬ В ИГРЕ",
                            "Магазин ресурсов • продажа • казино • промокоды • ежедневный бонус • достижения • статистика • сохранение прогресса в config.json")
        details.pack(fill="x", pady=(0, 12))
        tk.Label(details, text="Версия: 3.0", bg=PANEL, fg="#39e6a0",
                 font=("Segoe UI", 11, "bold")).pack(anchor="w", padx=15, pady=(0, 14))

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
