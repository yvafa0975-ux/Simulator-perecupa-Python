import time
import random
import json

SAVE_FILE = 'config.json'


def save_game(data):
    """Сохраняет все балансы в файл."""
    try:
        with open(SAVE_FILE, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
    except Exception:
        pass  # Игнорируем ошибки записи, чтобы игра не вылетала


def load_game():
    """Загружает все балансы.

    Если файла нет, выдает начальные.
    """
    try:
        with open(SAVE_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        # Стартовый баланс для нового игрока
        return {
            'moneybal': 1000,
            'robux_balance': 0,
            'golds_balance': 0,
            'gems_balance': 0,
            'shards_balance': 0,
            'TGStars_balance': 0,
        }
print("Тгк: @DvizhPERECUP")
time.sleep(2)
print("Пожалуйста, подождите 3 секунды!")
time.sleep(3)
print("Обновление global 2.0")
time.sleep(1)
print("Что добавлено: Новые валюты Gems/Shrads/TGStars, Сохранение в config! Исправление багов.") #Увед про обновку йоу
print("Привет")
time.sleep(1)
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
        input("Укажите пожалуйста (да/нет) :")

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
        input("Ознакомья со своими первыми деньгами! (Хочу!/Не надо!) :")

buy_items = "ничего"
itemsshop = ["Золото Standoff2", "Robux", "Gems", "Shards", "TGStars"]
robuxoffer = ["1,5 robux за 1 валюту!"]
goldsoffer = ["2 Golds за 1 валюту!"]
gemsoffer = ["1,5 Gems за 1 валюту!"]
shardsoffer = ["5 Shards за 1 валюту!"]
tgstarsoffer = ["2 stars за 1.39 валюты!"]
while True:
    print(f"Твой баланс, {moneybal}")
    print(f"Товары, {itemsshop}")
    print(f"1.Купить {itemsshop[0]} за {goldsoffer}")
    print(f"2.Купить {itemsshop[1]} за {robuxoffer}")
    print("3.Я хочу выйти из игры!")

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
    print(f"Твой баланс денег равен {moneybal}")
    print(f"Товары {itemsshop}")
    print(f"1.Купить {itemsshop[0]} за {goldsoffer}")
    print(f"2.Купить {itemsshop[1]} за {robuxoffer}")
    print(f"3.НОВОЕ! Продать робуксы {robux_balance} за 1.5р за один робукс!")
    print(f"4.НОВОЕ! Продать золото {golds_balance} за 1.5р за одно золото!")
    print("5.Я хочу выйти из игры")

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
    print("========== НОВОЕ МЕНЮ ==========")
    print(f"Твой баланс денег равен {moneybal}")
    print(f"Товары {itemsshop}")
    print(f"1.Купить {itemsshop[0]} за {goldsoffer}")
    print(f"2.Купить {itemsshop[1]} за {robuxoffer}")
    print(f"3.Продать робуксы {robux_balance} за 1.5р за один робукс!")
    print(f"4.Продать золото {golds_balance} за 1.5р за одно золото!")
    print("5.НОВОЕ! Казино")
    print("6.Я хочу выйти из игры")

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
            print("Все таки - ты решил заглянуть сюда")
            time.sleep(1)
            print(f"Не вздумай пробовать вливать сюда все деньги! Твой баланс равняется {moneybal}")
            print("Смотри, ты выбираешь от 1 до 2 и пишешь число, если угадал - приз удваивается, если просрал - деньга которую ты поставил исчезает(")
            casino = int(input("Сколько денег ты хочешь депнуть? :"))
            player_dep = input("Выбирай число (1/2) :")
            random_number = random.randint(1,2)
            if casino <= moneybal:
                print("Good")
            else:
                print("А про деньги то не подумал(у тя их нету)")
            if player_dep == "random_number":
                print(f"Что, ты угадал! Число {random_number}")
                moneybal = moneybal + (casino *2)
                print("Поздравляю, твой выйгрыш (casino *2)")
                break
            else:
                moneybal = moneybal - casino
                print(f"Увы, ты не угадал( Ты теряешь {casino}")
                print(f"Выйгрышное число было {random_number}")
                time.sleep(6)
                print("Жди апдейта")
                time.sleep(3)
                break
    elif actions_3 == "6":
        print("Прощай, друг")
        time.sleep(1)
        input("\nНажимай любую клавишу и ты выйдешь...")
        break
print("Как так вышло глобальное обновлениеи 2.0 - пора ознакомится с новыми функциями!")
print("Loading...")
time.sleep(10)
print("MENU 2.0")
time.sleep(2)
while True:
    print('\033[32m========== NEW MENU 2.0 ==========\033[0m')
    print(f'\033[32mТвой баланс {moneybal}\033[0m')
    print(f'\033[32mТовары {itemsshop}\033[0m')
    print(f'\033[32m1.Покупка {itemsshop[0]} За {goldsoffer}\033[0m')
    print(f'\033[32m2.Покупка {itemsshop[1]} За {robuxoffer}\033[0m')
    print(f'\033[32m3.НОВОЕ! Покупка {itemsshop[2]} За {gemsoffer}\033[0m')
    print(f'\033[32m4.НОВОЕ! Покупка {itemsshop[3]} За {shardsoffer}\033[0m')
    print(f'\033[32m5.НОВОЕ! Покупка {itemsshop[4]} За {tgstarsoffer}\033[0m')
    print(f'\033[32m6.Казино\033[0m')
    print(f'\033[32m7.Продать свои {robux_balance} Robux\033[0m')
    print(f'\033[32m8.Продать свои {golds_balance} Gold\033[0m')
    print('\033[32m9.Я хочу выйти из игры\033[0m')
    print(f'\033[32m10.Продать свои {gems_balance} Gems\033[0m')
    print(f'\033[32m11.Продать свои {shards_balance} Shards\033[0m')
    print(f'\033[32m12.Продать свои {TGStars_balance} TGStars\033[0m')

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
            break
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
            break
        else:
            print("Не хватает золота")
    elif actions_4 == "9":
        print("Прощай, друг")
        time.sleep(1)
        input("\nНажимай любую клавишу и ты выйдешь...")
    elif actions_4 == "10":
        sell_amount = int(input("Сколько хотите продать? :"))
        if gems_balance >= sell_amount:
            money_money = sell_amount *2.5
            gems_balance = gems_balance - sell_amount
            moneybal = moneybal + money_money
            time.sleep(1)
            print(f"Ты успешно продал {sell_amount}, теперь твой баланс денег {moneybal}")
            break
    elif actions_4 == "11":
        sell_amount = int(input("Сколько хотите продать? :"))
        if shards_balance >= sell_amount:
            money_money = sell_amount *6.1
            shards_balance = shards_balance - sell_amount
            moneybal = moneybal + money_money
            time.sleep(1)
            print(f"Ты успешно продал {sell_amount}, теперь твой баланс денег {moneybal}")
            break
    elif actions_4 == "12":
        sell_amount = int(input("Сколько хотите продать? :"))
        if TGStars_balance >= sell_amount:
            money_money = sell_amount *2
            TGStars_balance = TGStars_balance - sell_amount
            moneybal = moneybal + money_money
            time.sleep(1)
            print(f"Ты успешно продал {sell_amount}, теперь твой баланс денег {moneybal}")
            break
while True:
    print("2.0 НАСТУПАЕТ")
    time.sleep(1)
    print("500 строк...")
    time.sleep(2)
    print("Представляю внимание - движок Симулятор перекупа")
    time.sleep(2)
    print("В менюшку!")
    break

        








