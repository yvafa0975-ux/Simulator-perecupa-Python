import time
import random
import json

SAVE_FILE = 'config.json'


def save_game(data):
    try:
        with open(SAVE_FILE, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
    except Exception:
        pass  


def load_game():
    """Загружает все балансы.

    Если файла нет, выдает начальные.
    """
    try:
        with open(SAVE_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return {
            'moneybal': 1000,
            'robux_balance': 0,
            'golds_balance': 0,
            'gems_balance': 0,
            'shards_balance': 0,
            'TGStars_balance': 0,
        }
GREEN = "\033[32m"
CYAN = "\033[36m"
RESET = "\033[0m"
YELLOW = "\033[33m"

print(f"{CYAN}  ____  _____ ____  _____ _  ___   _ ____    ____       ____  {RESET}")
print(f"{CYAN} |  _ \| ____|  _ \| ____| |/ / | | |  _ \  |___ \  _  |___ \ {RESET}")
print(f"{CYAN} | |_) |  _| | |_) |  _| | ' /| | | | |_) |   __) |(_)   __) |{RESET}")
print(f"{CYAN} |  __/| |___|  _ <| |___| . \| |_| |  __/   / __/  _   / __/ {RESET}")
print(f"{CYAN} |_|   |_____|_| \_\_____|_|\_\\\\___/|_|     |_____|(_) |_____|{RESET}")
time.sleep(0.5)
print(f"{GREEN}┌────────────────────────────────────────┐{RESET}")
print(f"{GREEN}│       СИМУЛЯТОР ПЕРЕКУПА 2.2           │{RESET}")
print(f"{GREEN}│         Тгк: @DvizhPERECUP             │{RESET}")
print(f"{GREEN}└────────────────────────────────────────┘{RESET}")
time.sleep(3)
print("Пожалуйста, подождите 3 секунды!")
time.sleep(3)
print("Обновление global 2.2")
time.sleep(1)
print(f"\n{YELLOW}┌────────────────────────────────────────┐{RESET}")
print(f"{YELLOW}│            ЧТО ДОБАВЛЕНО:              │{RESET}")
print(f"{YELLOW}├────────────────────────────────────────┤{RESET}")
print(f"{YELLOW}│ • Исправление багов                    │{RESET}")
print(f"{YELLOW}│ • Первый интерфейс                     │{RESET}")
print(f"{YELLOW}└────────────────────────────────────────┘{RESET}\n")
print("Привет")
time.sleep(1)

game_data = load_game() #Для тех кто открыл код - это просто сохрание системное
moneybal = game_data['moneybal']
robux_balance = game_data['robux_balance']
golds_balance = game_data['golds_balance']
gems_balance = game_data['gems_balance']
shards_balance = game_data['shards_balance']
TGStars_balance = game_data['TGStars_balance']

answer = input("Будете играть (да/нет) :")
while True:
    if answer == "да":
        print("Отлично, игра называется Симулятор перекупа!")
        input("Продолжаем!(нажмите Enter клавишу)")
        time.sleep(3)
        break
    elif answer == "нет":
        print("К сожалению, вы не хотите играть")
        input("\nНажмите любую клавишу для выхода...")
        break
    else:
        print("Вы указали не ту команду")
        answer = input("Укажите пожалуйста (да/нет) :")

moneybal = 1000
robux_balance = 0
golds_balance = 0
gems_balance = 0
shards_balance = 0
TGStars_balance = 0
moneybalance = input("Ознакомься со своими первыми деньгами! (Хочу!/Не надо!) :")
while True:
    if moneybalance == "Хочу!":
        print("Тебе дается первая 1000!")
        time.sleep(2)
        print("Это реально замечательно для старта!")
        break
    elif moneybalance == "Не надо!":
        print("Жаль, что ты не хочешь продолжать путь(")
        input("\nНажмите любую клавишу для выхода...")
        break
    else:
        print("Я тебя чуть чуть не понял(...")
        moneybalance = input("Ознакомья со своими первыми деньгами! (Хочу!/Не надо!) :")

buy_items = "ничего"
itemsshop = ["Золото Standoff2", "Robux", "Gems", "Shards", "TGStars"]
robuxoffer = ["1,5 robux за 1 валюту!"]
goldsoffer = ["2 Golds за 1 валюту!"]
gemsoffer = ["1,5 Gems за 1 валюту!"]
shardsoffer = ["5 Shards за 1 валюту!"]
tgstarsoffer = ["2 stars за 1.39 валюты!"]
while True:
    NEW_TAG = f"{YELLOW}[НОВОЕ!]{RESET}"
    items_to_show = f"{itemsshop[0]} и {itemsshop[1]}"
    print(f"{CYAN}╭────────────────────────────────────────────────────────────╮{RESET}")
    print(f"{CYAN}│{RESET}  {YELLOW}💰 Твой баланс денег равен:{RESET} {moneybal!s:<34} {CYAN}│{RESET}")
    print(f"{CYAN}│{RESET}  {YELLOW}📦 Доступные товары:{RESET}       {items_to_show:<43} {CYAN}│{RESET}")
    print(f"{CYAN}├────────────────────────────────────────────────────────────┤{RESET}")
    print(f"{CYAN}│{RESET}  {GREEN}1.{RESET} Купить {itemsshop[0]!s:<15} за {goldsoffer!s:<24} {CYAN}│{RESET}")
    print(f"{CYAN}│{RESET}  {GREEN}2.{RESET} Купить {itemsshop[1]!s:<15} за {robuxoffer!s:<24} {CYAN}│{RESET}")
    print(f"{CYAN}│{RESET}  {GREEN}3.{RESET} 🚪 Я хочу выйти из игры                                  {CYAN}│{RESET}")
    print(f"{CYAN}╰────────────────────────────────────────────────────────────╯{RESET}")

    actions = input("Выбирите следуйщие действия (1/2/3) :")
    amount = int(input("Сколько валюты вы планируете потратить?"))
    if actions == "1":
        print("Отлично")
        time.sleep(2)
        input("Сколько хотите купить? :")
        if moneybal >= amount:
            moneybal = moneybal - amount
            golds_send = amount *2
            golds_balance = golds_balance + golds_send
            buy_items = "Golds"
            print(f"Ты успешно купил Золото! {golds_send}")
        else:
            ("У тебя не хватает деняк(")
    elif actions == "2":
        amount = int(input("Сколько валюты вы планируете потратить?"))
        if moneybal >= amount:
            moneybal = moneybal - amount
            robux_send = amount *1.5
            robux_balance = robux_balance + robux_send
            buy_items = "Robux"
            print(f"Ты успешно купил Robux! {robux_send}")
        else:
            print("У тебя не хватает деняк(")
    elif actions == "3":
        input("\nНажмите любую клавишу чтобы выйти...")
    break

while True:
    if buy_items == "Golds":
        print(f"Отлично, ты купил {golds_balance} и теперь твой баланс деняк равен {moneybal}")
        time.sleep(1)
        break
    elif buy_items == "Robux":
        print(f"Отлично, ты купил {robux_balance} и теперь твой баланс деняк равен {moneybal}")
        time.sleep(1)
        break
    else:
        print(f"Ты нечего не купил, твои балансы: Голды {golds_balance} Робуксов {robux_balance} Деняк {moneybal}")
        break

print("Тебе открылась возможность - продавать это все дело!")
time.sleep(2)
print("Смотри на свое новое меню!")
time.sleep(1)

while True:
    NEW_TAG = f"{YELLOW}[НОВОЕ!]{RESET}"
    show_to_items = f"{itemsshop[0]} и {itemsshop[1]}"
    print(f"{CYAN}╭────────────────────────────────────────────────────────────────────────╮{RESET}")
    print(f"{CYAN}│{RESET}  {YELLOW}💰 Твой баланс денег равен:{RESET} {moneybal!s:<43} {CYAN}│{RESET}")
    print(f"{CYAN}│{RESET}  {YELLOW}📦 Доступные товары:{RESET}       {show_to_items:<43} {CYAN}│{RESET}")
    print(f"{CYAN}├────────────────────────────────────────────────────────────────────────┤{RESET}")
    print(f"{CYAN}│{RESET}  {GREEN}1.{RESET} Купить {itemsshop[0]!s:<18} за {goldsoffer!s:<38} {CYAN}│{RESET}")
    print(f"{CYAN}│{RESET}  {GREEN}2.{RESET} Купить {itemsshop[1]!s:<18} за {robuxoffer!s:<38} {CYAN}│{RESET}")
    print(f"{CYAN}├────────────────────────────────────────────────────────────────────────┤{RESET}")
    print(f"{CYAN}│{RESET}  {GREEN}3.{RESET} {NEW_TAG} Продать робуксы ({robux_balance!s}) за 1.5р за 1 шт.               {CYAN}│{RESET}")
    print(f"{CYAN}│{RESET}  {GREEN}4.{RESET} {NEW_TAG} Продать золото ({golds_balance!s}) за 1.5р за 1 шт.                {CYAN}│{RESET}")
    print(f"{CYAN}├────────────────────────────────────────────────────────────────────────┤{RESET}")
    print(f"{CYAN}│{RESET}  {GREEN}5.{RESET} 🚪 Я хочу выйти из игры                                              {CYAN}│{RESET}")
    print(f"{CYAN}╰────────────────────────────────────────────────────────────────────────╯{RESET}")

    actions_2 = input("Выбери действия 1/2/3/4/5 :")
    if actions_2 == "1":
        print("Good")
        time.sleep(1)
        amount = int(input("Сколько хотите купить золота?:"))
        if moneybal >= amount:
            moneybal = moneybal - amount
            golds_send = amount*2
            golds_balance = golds_balance + golds_send
            buy_items = "Golds"
            time.sleep(1)
            print(f"Ты успешно купил {golds_send} Золота!")
            break
        else:
            print("У тебя не хватает денег(")
            time.sleep(1)
            print("Скоро обновление! Где не нужно будет перезапускать симулятор+сохранение!")
            input("\nНажмите любую клавишу для выхода...")
            exit()
            break
    elif actions_2 == "2":
        print("Good")
        time.sleep(1)
        amount = int(input("Сколько хотите купить Robux?:"))
        if moneybal >= amount:
            moneybal = moneybal - amount
            robux_send = amount*1.5
            robux_balance = robux_balance + robux_send
            buy_items = "Robux"
            time.sleep(1)
            print(f"Ты успешно купил {robux_send} Robux!")
            break
        else:
            print("У тебя не хватает денег")
            time.sleep(1)
            print("Скоро обновление! Где не нужно будет перезапускать симулятор+сохранение!")
            input("\nНажмите любую клавишу для выхода...")
            exit()
    elif actions_2 == "3":
        print("Поздравляю с новой возможностью!")
        time.sleep(1)
        sell_amount = int(input("Сколько хотите продать? :"))
        if robux_balance >= sell_amount:
            money_money = sell_amount *1.5
            robux_balance = robux_balance - sell_amount
            moneybal = moneybal + money_money
            time.sleep(1)
            print(f"Ты успешно продал {sell_amount}, теперь твой баланс денег {moneybal}")
            break
        else:
            print("У тебя нету столько робаксов(")
            time.sleep(1)
            print("К сожалению, деватья не куда(")
            input("\nНажми любую клавишу для выхода...")
            exit()
    elif actions_2 == "4":
        print("Поздравляю с новой возможностью!")
        time.sleep(1)
        sell_amount = int(input("Сколько хотите продать золота? :"))
        if golds_balance >= sell_amount:
            money_money = sell_amount *2
            golds_balance = golds_balance - sell_amount
            moneybal = moneybal + money_money
            time.sleep(1)
            print(f"Ты успешно продал {sell_amount}, теперь твой баланс денег равен {moneybal}")
            break
        else:
            print("К сожалению, деваться не куда(")
            time.sleep(1)
            input("\nНажми на любую клавишу для выхода...")
    elif actions_2 == "5":
        print("Прощай, друг")
        time.sleep(1)
        input("\nНажимай любую клавишу и ты выйдешь...")
        break
print("Отлично, ты заработал свой первые деньги!")
time.sleep(1)
print("Теперь,чтобы мои старания на ветер не уходили - я сделал специально казино!")
time.sleep(1)
print("Все эти задержки - это time.sleep")
time.sleep(1)
print("Пора тебе ознакомится...")
questons = input("Ты готов? (да/нет) :")
while True:
    if questons == "да":
        print("Хорошо!")
        time.sleep(1)
        print("Для казино, мне потребовалась библиотека random")
        break
    elif questons == "нет":
        print("Извиняй, обнову не выкатил.")
        time.sleep(1)
        input("\nНажми любую клавишу для выхода...")
        break
    else:
        print("Отвечай нормально")
        questons = input("Ответь (да/нет) :")

while True:
    NEW_TAG = f"{YELLOW}[НОВОЕ!]{RESET}"

    price_1 = goldsoffer[0] if isinstance(goldsoffer, list) and goldsoffer else goldsoffer
    price_2 = robuxoffer[0] if isinstance(robuxoffer, list) and robuxoffer else robuxoffer

    items_to_show = f"{itemsshop[0]} и {itemsshop[1]}"

    opt_3 = f"Продать робуксы ({robux_balance!s}) за 1.5р за 1 шт."
    opt_4 = f"Продать золото ({golds_balance!s}) за 1.5р за 1 шт."
    opt_5 = f"{NEW_TAG} 🎰 Казино"
    opt_6 = "🚪 Я хочу выйти из игры"

    print(f"{CYAN}╭─────────────────── {YELLOW}NEW MENU VISUAL 2.2{CYAN} ───────────────────╮{RESET}")
    print(f"{CYAN}│{RESET}  {YELLOW}💰 Твой баланс денег равен:{RESET} {moneybal!s:<34} {CYAN}│{RESET}")
    print(f"{CYAN}│{RESET}  {YELLOW}📦 Доступные товары:{RESET}       {items_to_show!s:<34} {CYAN}│{RESET}")
    print(f"{CYAN}├────────────────────────────────────────────────────────────┤{RESET}")
    print(f"{CYAN}│{RESET}  {GREEN}1.{RESET} Купить {itemsshop[0]!s:<15} за {price_1!s:<24} {CYAN}│{RESET}")
    print(f"{CYAN}│{RESET}  {GREEN}2.{RESET} Купить {itemsshop[1]!s:<15} за {price_2!s:<24} {CYAN}│{RESET}")
    print(f"{CYAN}├────────────────────────────────────────────────────────────┤{RESET}")
    print(f"{CYAN}│{RESET}  {GREEN}3.{RESET} {opt_3:<55} {CYAN}│{RESET}")
    print(f"{CYAN}│{RESET}  {GREEN}4.{RESET} {opt_4:<55} {CYAN}│{RESET}")
    print(f"{CYAN}├────────────────────────────────────────────────────────────┤{RESET}")
    print(f"{CYAN}│{RESET}  {GREEN}5.{RESET} {opt_5:<64} {CYAN}│{RESET}")
    print(f"{CYAN}│{RESET}  {GREEN}6.{RESET} {opt_6:<55} {CYAN}│{RESET}")
    print(f"{CYAN}╰────────────────────────────────────────────────────────────╯{RESET}")

    actions_3 = input("Выберите действия (1/2/3/4/5/6) :")
    if actions_3 == "1":
            print("Good")
            time.sleep(1)
            amount = int(input("Сколько хотите купить золота?:"))
            if moneybal >= amount:
                moneybal = moneybal - amount
                golds_send = amount*2
                golds_balance = golds_balance + golds_send
                buy_items = "Golds"
                time.sleep(1)
                print(f"Ты успешно купил {golds_send} Золота!")
                break
            else:
                print("У тебя не хватает денег(")
                time.sleep(1)
                print("Скоро обновление! Где не нужно будет перезапускать симулятор+сохранение!")
                input("\nНажмите любую клавишу для выхода...")
                exit()
                break
    elif actions_3 == "2":
        print("Good")
        time.sleep(1)
        amount = int(input("Сколько хотите купить Robux?:"))
        if moneybal >= amount:
            moneybal = moneybal - amount
            robux_send = amount*1.5
            robux_balance = robux_balance + robux_send
            buy_items = "Robux"
            time.sleep(1)
            print(f"Ты успешно купил {robux_send} Robux!")
            break
        else:
            print("У тебя не хватает денег")
            time.sleep(1)
            print("Скоро обновление! Где не нужно будет перезапускать симулятор+сохранение!")
            input("\nНажмите любую клавишу для выхода...")
            exit()
    elif actions_3 == "3":
        print("Поздравляю с новой возможностью!")
        time.sleep(1)
        sell_amount = int(input("Сколько хотите продать? :"))
        if robux_balance >= sell_amount:
            money_money = sell_amount *1.5
            robux_balance = robux_balance - sell_amount
            moneybal = moneybal + money_money
            time.sleep(1)
            print(f"Ты успешно продал {sell_amount}, теперь твой баланс денег {moneybal}")
            break
        else:
            print("У тебя нету столько робаксов(")
            time.sleep(1)
            print("К сожалению, деватья не куда(")
            input("\nНажми любую клавишу для выхода...")
            exit()
    elif actions_3 == "4":
        print("Поздравляю с новой возможностью!")
        time.sleep(1)
        sell_amount = int(input("Сколько хотите продать золота? :"))
        if golds_balance >= sell_amount:
            money_money = sell_amount *2
            golds_balance = golds_balance - sell_amount
            moneybal = moneybal + money_money
            time.sleep(1)
            print(f"Ты успешно продал {sell_amount}, теперь твой баланс денег равен {moneybal}")
            break
        else:
            print("К сожалению, деваться не куда(")
            time.sleep(1)
            input("\nНажми на любую клавишу для выхода...")
    elif actions_3 == "5":
            print(f"Не вздумай пробовать вливать сюда все деньги! Твой баланс равняется {moneybal}")
            print("Смотри, ты выбираешь от 1 до 2 и пишешь число, если угадал - приз удваивается, если просрал - деньга которую ты поставил исчезает(")
            casino = int(input("Сколько денег ты хочешь депнуть? :"))
            if casino > moneybal:
                print("А про деньги то не подумал(у тя их нету)")
            elif casino <= 0:
                print("Нельзя ставить ноль или отрицательную сумму!")
            else:
                player_dep = int(input("Выбирай число (1/2) :")) 
                random_number = random.randint(1, 2)
            if player_dep == random_number:
                print(f"Что, ты угадал! Число {random_number}")
                moneybal = moneybal + casino 
                print(f"Поздравляю, твой выйгрыш {casino * 2}")
            else:
                moneybal = moneybal - casino 
                print(f"Увы, ты не угадал( Ты теряешь {casino}")
                print(f"Выйгрышное число было {random_number}")
                break
    elif actions_3 == "6":
        print("Прощай, друг")
        time.sleep(1)
        input("\nНажимай любую клавишу и ты выйдешь...")
        break
print("Как так вышло глобальное обновлениеи 2.0 - пора ознакомится с новыми функциями!")
print("Loading...")
time.sleep(10)
print("MENU 2.0(Стиль меню был обновлен в 2.2)")
time.sleep(2)
while True:
    print('\033[32m=================== NEW MENU VISUAL 2.2 ===================\033[0m')
    print(f'\033[32m💵 РУБЛИ: \033[36m{moneybal}р\033[0m')
    print(f'\033[32m🎒 ЗАПАСЫ: \033[33mGold: {golds_balance} | Robux: {robux_balance} | Gems: {gems_balance} | Shards: {shards_balance} | Stars: {TGStars_balance}\033[0m')
    print('\033[32m---------------------------------------------------\033[0m')
    print(f'\033[32m[1] 🛒 Купить {itemsshop[0]} ➔ {goldsoffer}\033[0m')
    print(f'\033[32m[2] 🛒 Купить {itemsshop[1]} ➔ {robuxoffer}\033[0m')
    print(f'\033[32m[3] 🔥 Купить {itemsshop[2]} ➔ {gemsoffer}\033[0m')
    print(f'\033[32m[4] 🔥 Купить {itemsshop[3]} ➔ {shardsoffer}\033[0m')
    print(f'\033[32m[5] 🔥 Купить {itemsshop[4]} ➔ {tgstarsoffer}\033[0m')
    print('\033[32m---------------------------------------------------\033[0m')
    print(f'\033[32m[7]  💰 Продать Robux   ({robux_balance} шт.)\033[0m')
    print(f'\033[32m[8]  💰 Продать Gold    ({golds_balance} шт.)\033[0m')
    print(f'\033[32m[10] 💰 Продать Gems    ({gems_balance} шт.)\033[0m')
    print(f'\033[32m[11] 💰 Продать Shards  ({shards_balance} шт.)\033[0m')
    print(f'\033[32m[12] 💰 Продать TGStars ({TGStars_balance} шт.)\033[0m')
    print('\033[32m---------------------------------------------------\033[0m')
    print(f'\033[32m[6] 🎰 ИГРАТЬ В КАЗИНО\033[0m')
    print(f'\033[31m[9] 🚪 СОХРАНИТЬСЯ И ВЫЙТИ\033[0m')
    print('\033[32m===================================================\033[0m')
    actions_4 = input("Выбери действия (1/2/3/4/5/6/7/8/9/10/11/12) :")
    if actions_4 == "1":
        print("Good")
        time.sleep(1)
        amount = int(input("Сколько хотите купить золота?:"))
        if moneybal >= amount:
            moneybal = moneybal - amount
            golds_send = amount*2
            golds_balance = golds_balance + golds_send
            buy_items = "Golds"
            time.sleep(1)
            print(f"Ты успешно купил {golds_send} Золота!")
            break
        else:
            print("У тебя не хватает денег(")
            time.sleep(1)
            print("Выход 2.0 версии")
    elif actions_4 == "2":
        print("Good")
        time.sleep(1)
        amount = int(input("Сколько хотите купить Robux?:"))
        if moneybal >= amount:
            moneybal = moneybal - amount
            robux_send = amount*1.5
            robux_balance = robux_balance + robux_send
            buy_items = "Robux"
            time.sleep(1)
            print(f"Ты успешно купил {robux_send} Robux!")
            break
        else:
            print("У тебя не хватает денег(")
            time.sleep(1)
            print("Выход 2.0 версии")
    elif actions_4 == "3":
        print("Good")
        time.sleep(1)
        amount = int(input("Сколько хотите купить Gems?:"))
        if moneybal >= amount:
            moneybal = moneybal - amount
            gems_send = amount*1.5
            gems_balance = gems_balance + gems_send
            buy_items = "Gems"
            time.sleep(1)
            print(f"Ты успешно купил {gems_send} Gems!")
            break
        else:
            print("У тебя не хватает денег(")
            time.sleep(1)
            print("Выход 2.0 версии")
    elif actions_4 == "4":
        print("Good")
        time.sleep(1)
        amount = int(input("Сколько хотите купить Shards?:"))
        if moneybal == amount:
            moneybal = moneybal - amount
            shards_send = amount*5
            shards_balance = shards_balance + shards_send
            buy_items = "Shards"
            time.sleep(1)
            print(f"Ты успешно купил {shards_send} Shards!")
            break
        else:
            print("У тебя не хватает денег(")
            time.sleep(1)
            print("Выход 2.0 версии")
    elif actions_4 == "5":
        print("Good")
        time.sleep(1)
        amount = int(input("Сколько вы хотите купить TGStars?:"))
        if moneybal == amount:
            moneybal = moneybal - amount
            tgstars_send = amount*2
            TGStars_balance = TGStars_balance + tgstars_send
            buy_items = "TGStars"
            time.sleep(1)
            print(f"Ты успешно купил {tgstars_send} TGStars!")
            break
        else:
            print("У тебя не хватает денег(")
            time.sleep(1)
            print("Выход 2.0 версии")
    elif actions_4 == "6":
            print(f"Не вздумай пробовать вливать сюда все деньги! Твой баланс равняется {moneybal}")
            print("Смотри, ты выбираешь от 1 до 2 и пишешь число, если угадал - приз удваивается, если просрал - деньга которую ты поставил исчезает(")
            casino = int(input("Сколько денег ты хочешь депнуть? :"))
            if casino > moneybal:
                print("А про деньги то не подумал(у тя их нету)")
            elif casino <= 0:
                print("Нельзя ставить ноль или отрицательную сумму!")
            else:
                player_dep = int(input("Выбирай число (1/2) :")) 
                random_number = random.randint(1, 2)
            if player_dep == random_number:
                print(f"Что, ты угадал! Число {random_number}")
                moneybal = moneybal + casino 
                print(f"Поздравляю, твой выйгрыш {casino * 2}")
            else:
                moneybal = moneybal - casino 
                print(f"Увы, ты не угадал( Ты теряешь {casino}")
                print(f"Выйгрышное число было {random_number}")
                break
    elif actions_4 == "7":
        sell_amount = int(input("Сколько хотите продать? :"))
        if robux_balance >= sell_amount:
            money_money = sell_amount *1.5
            robux_balance = robux_balance - sell_amount
            moneybal = moneybal + money_money
            time.sleep(1)
            print(f"Ты успешно продал {sell_amount}, теперь твой баланс денег {moneybal}")
        else:
            print("У тебя нету столько робаксов")
    elif actions_4 == "8":
        sell_amount = int(input("Сколько хотите продать золота? :"))
        if golds_balance >= sell_amount:
            money_money = sell_amount *2
            golds_balance = golds_balance - sell_amount
            moneybal = moneybal + money_money
            time.sleep(1)
            print(f"Ты успешно продал {sell_amount}, теперь твой баланс денег равен {moneybal}")
        else:
            print("Не хватает золота")
    elif actions_4 == "9":
        print("Прощай, друг")
        time.sleep(1)
        input("\nНажимай любую клавишу и ты выйдешь...")
        exit()
    elif actions_4 == "10":
        sell_amount = int(input("Сколько хотите продать? :"))
        if gems_balance >= sell_amount:
            money_money = sell_amount *2.5
            gems_balance = gems_balance - sell_amount
            moneybal = moneybal + money_money
            time.sleep(1)
            print(f"Ты успешно продал {sell_amount}, теперь твой баланс денег {moneybal}")
    elif actions_4 == "11":
        sell_amount = int(input("Сколько хотите продать? :"))
        if shards_balance >= sell_amount:
            money_money = sell_amount *6.1
            shards_balance = shards_balance - sell_amount
            moneybal = moneybal + money_money
            time.sleep(1)
            print(f"Ты успешно продал {sell_amount}, теперь твой баланс денег {moneybal}")
    elif actions_4 == "12":
        sell_amount = int(input("Сколько хотите продать? :"))
        if TGStars_balance >= sell_amount:
            money_money = sell_amount *2
            TGStars_balance = TGStars_balance - sell_amount
            moneybal = moneybal + money_money
            time.sleep(1)
            print(f"Ты успешно продал {sell_amount}, теперь твой баланс денег {moneybal}")
while True:
    print(f"\n{GREEN}┌────────────────────────────────────────┐{RESET}")
    print(f"{GREEN}│             GLOBAL UPDATE 2.2          │{RESET}")
    print(f"{GREEN}├────────────────────────────────────────┤{RESET}")
    print(f"{GREEN}│ {YELLOW}• Версия 2.2 официально ВЫШЛА!{GREEN}         │{RESET}")
    print(f"{GREEN}│   Эта обнова получилась очень хорошей. │{RESET}")
    print(f"{GREEN}│                                        │{RESET}")
    print(f"{GREEN}│ {CYAN}• ЧТО ДАЛЬШЕ?{GREEN}                          │{RESET}")
    print(f"{GREEN}│   Следующая версия игры будет          │{RESET}")
    print(f"{GREEN}│   ПОЛНОСТЬЮ ПЕРЕПИСАННАЯ с нуля!       │{RESET}")
    print(f"{GREEN}│                                        │{RESET}")
    print(f"{GREEN}│ {YELLOW}• СКОРО:{GREEN}                               │{RESET}")
    print(f"{GREEN}│   Уже вовсю готовится НАСТОЯЩИЙ        │{RESET}")
    print(f"{GREEN}│   ГРАФИЧЕСКИЙ ИНТЕРФЕЙС (GUI)!         │{RESET}")
    print(f"{GREEN}└────────────────────────────────────────┘{RESET}\n")

    line1 = f" {YELLOW}• GLOBAL UPDATE 2.3 SOON!{RESET}"
    line2 = "   Уже вовсю готовится мощное"
    line3 = "   и самое крупное обновление!"
    line4 = f" {CYAN}• ЧТО БУДЕТ ДОБАВЛЕНО?{RESET}"
    line5 = f"   Первый полноценный {YELLOW}графический{RESET}"
    line6 = f"   {YELLOW}интерфейс (GUI){RESET} приложения!"
    line7 = "   Тотальный фикс старых багов."
    line8 = f"   Уникальные {GREEN}новые фичи{RESET} и механики!"

    print(f"\n{GREEN}┌────────────────────────────────────────┐{RESET}")
    print(f"{GREEN}│            GLOBAL UPDATE 2.3           │{RESET}")
    print(f"{GREEN}├────────────────────────────────────────┤{RESET}")
    print(f"{GREEN}│{RESET}{line1:<49}{GREEN}│{RESET}")
    print(f"{GREEN}│{RESET}{line2:<40}{GREEN}│{RESET}")
    print(f"{GREEN}│{RESET}{line3:<40}{GREEN}│{RESET}")
    print(f"{GREEN}│                                        │")
    print(f"{GREEN}│{RESET}{line4:<49}{GREEN}│{RESET}")
    print(f"{GREEN}│{RESET}{line5:<49}{GREEN}│{RESET}")
    print(f"{GREEN}│{RESET}{line6:<49}{GREEN}│{RESET}")
    print(f"{GREEN}│{RESET}{line7:<40}{GREEN}│{RESET}")
    print(f"{GREEN}│{RESET}{line8:<49}{GREEN}│{RESET}")
    print(f"{GREEN}└────────────────────────────────────────┘{RESET}\n")
#хеххе 617