print("Приветсвуем в текстовой игре!")
print("Ваша задача: не допустить чтобы вы (кот) умер.")
print("============================================", end="")
print("=====================================================")
print("Котик родился.")
print("У вас есть 3 жизни.")
print("Выберете изначальную судьбу: 'быть бездомным' или 'быть домашним'")
print("1) быть бездомным")
print("2) быть домашним")
lives = 3


def homeless(lives):
    if lives > 0:
        print("Достижение - ВЫ УЛИЧНЫЙ КОТ")
        print("Кот - бомжик.")
        print("Вам нечего есть.")
        print("Выберете что съесть:")
        print("1) молоко")
        print("2) поймать крысу или мышь")
        eda = input()
        if eda == "1":
            print("Молоко это не еда... Вы этим не наелись и поэтому вы умерли. ", end="")
            print("+ Молоко было просроченное.")
            print("Вы помёрли.")
            lives = 0
        elif eda == "2":
            print("Вы поймали крысу и приготовили её.")
            print("+НАВЫК ГОТОВКИ")
            print("На запах прилетела чайка. Она тоже хочет есть и готова драться за еду!")
            print("Отдать еду?")
            print("1) Нет!")
            print("2) Да")
            neda = input()
            while neda != "1" and neda != "2":
                print("Но-но-но! Это как вообще? Выберете 1 или 2.")
                neda = input()
            if neda == "1":
                print("На вас напали и вы немножко проиграли битву.")
                print("Ну в общем - R.I.P.")
                lives = 0
            elif neda == "2":
                print("Вы отдали еду.")
                print("На запах прилетело ещё 2 чайки.")
                print("Они были голодные и подумали что вы еда.")
                print("Вас схватили.")
                print("Сейчас вы летите над городом в когтях чайки.")
                print("Вас не поделили и теперь вы летите вниз.")
        else:
            print("Такого варианта нет.")
            print("Вы слишком долго думали...")
            print("You died.")
            lives = 0
    return lives


def homik(lives):
    if lives > 0:
        print("Вы очнулись в квартире")
        print("+НАВЫК ДОМАШНИЙ КОТ")
        print("Чтобы претвориться нормальным котом введите 'мяу'")
        miv = input()
        while miv != "мяу" and miv != "Мяу":
            print("Что за кот? Попробуйте ещё раз")
            miv = input()
        print("Отлично! Вы вроде смышлённый.")
        print("Теперь напишите сочинение на тему 'Я кот'.")
        sochin = input()
        while len(sochin) < 50:
            print("Маловато будет...")
            sochin = input()
        print("Отличная ночная опера!")
        print("Т.к. сейчас ночь, почему бы не побегать?")
        print("Побегаем?")
        print("1) Нет! Люди же спят!")
        print("2) Да!")
        da = input()
        if da == "1":
            print("Что за вопросы? КОНЕЧНО ПОБЕГАЕМ!")
        print("Супер!")
        print("Уже нет...")
        print("Вы разбили стакан.")
        print("Ваша задача быстро убежать.")
        print("Куда бежать?")
        print("1) На улицу!")
        print("2) Нападение - самая лучшая защита!")
        print("3) Меня простят.")
        print("4) Ну у меня же лапки! +я котик")
        kyda = input()
        while kyda != "1" and kyda != "2" and kyda != "3" and kyda != "4":
            print("Что за кот? Попробуйте ещё раз")
            kyda = input()
        if kyda == "1" or kyda == "2":
            print("Ну что сказать... Вы теперь на улице.")
        else:
            print("Вы были элегантны, поэтому вы теперь на улице с рыбкой в запазухе.")
            print("Вы были слишком шумные поэтому...")
    return lives


def end(lives):
    print("Что ж, вы были и бездомным и 'домным')")
    print("Вы научились многому!")
    print("Посмотрим,справитесь ли вы с последним заданием.")
    print("Сколько корней у квадратного уравнения: x^2 - 6x + 9")
    print("1) один")
    print("2) два")
    otv = input()
    while otv != "1" and otv != "2":
        print("Это мы не прохидили! Это нам не задавали")
        print("Введите 1 или 2")
        otv = input()
    if otv == "1":
        print("Вы выйграли!")
        print("Ураааааааааааа!")
    else:
        print("Неа, математик...")

statys = input()
while statys != "1" and statys != "2":
    print("Но-но-но! Это как вообще? Выберете 1 или 2.")
    statys = input()
if statys == "1":
    lives = homeless(lives)
    lives = homik(lives)
elif statys == "2":
    lives = homik(lives)
    lives = homeless(lives)
if lives > 0:
    end(lives)
input()
