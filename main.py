import time
print('Перед тобой три пути и на каждом из них тебя ждёт уникальное испытание!')
print('')
print('Первая дорога приведёт тебя к кроважадному монстру.\nВторая дорога ведёт в густую чащу леса, в которой ты сможешь обрести силу.\nТретья дорога является старой пыльной дорожкой по которой раньше ездили торговцы.' )
print('')
print('Так вот, путник, какую тропу ты выбираешь? ')
weapon = 0
amul = 0
print('Выбирите номер\n1.\n2.\n3.')
choice = int(input())
if choice == 1:
    if weapon == 1:
        print()
    else:
        print('Ты ещё слишком слаб и у тебя нет оружия, ты не можешь сразиться с монстром!')
        print('Возвращайся позже')
if choice == 2:
    print('Посреди леса ты встречаешь легендарный меч, застрявший в камнях на века.')
    time.sleep(1.5)
    print('Тут из-за дерева выпрыгивает гоблин охраняющий этот меч')
    time.sleep(2)
    print('⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿')
    print('⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿')
    print('⣿⡏⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⢹⣿')
    print('⣿⡇⠄⠙⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⠄⢸⣿')
    print('⣿⡇⢰⣆⠈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠁⣰⡆⢸⣿')
    print('⣿⡇⢸⣿⣷⡄⠈⠻⣿⣿⣿⣿⣿⣿⠿⠿⣿⣿⣿⣿⣿⣿⠟⠁⢠⣾⣿⡇⢸⣿')
    print('⣿⣇⠄⣿⠋⠛⢦⠄⠈⠉⠉⠁⠄⠄⠄⠄⠄⠄⠈⠉⠉⠁⠄⡴⠛⠙⣿⠄⣸⣿')
    print('⣿⣿⡄⠹⡄⠄⠄⠄⠄⣠⣶⣶⣦⡀⠄⠄⢀⣴⣾⣶⣄⠄⠄⠄⠄⢠⠏⢠⣿⣿')
    print('⣿⣿⣿⣄⠙⠲⠄⠄⠐⠛⠋⠉⠛⠓⠄⠄⠚⠛⠉⠙⠛⠂⠄⠄⠖⠋⣠⣿⣿⣿')
    print('⣿⣿⣿⣿⣷⣶⣶⠄⠄⣶⣄⠄⢠⣶⣶⣶⣦⡀⢀⣠⣶⠄⠄⣶⣶⣾⣿⣿⣿⣿')
    print('⣿⣿⣿⣿⣿⣿⣟⡀⠄⠈⠻⢷⣿⣿⣿⠻⣿⣷⡿⠟⠁⠄⢀⣹⣿⣿⣿⣿⣿⣿')
    print('⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣤⣄⣀⠈⠁⠄⠄⣀⣠⣤⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿')
    print('⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿')
    print('⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿')
    print('⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿')
    print('Гоблин - <<Только достойный боец сможет обрести силу этого меча!>>')
    print('Гоблин - <<Победи меня в бою и он твой>>')

    hp = 100
    hp_g = 100
    from random import *



    print(f"HP Гоблина - {hp_g}")
    print()
    while True:
        if all([hp > 0, hp_g > 0]):
            punch = int(
            input("выберите место для удара:\n      1) голова; \n      2) туловище; \n      1) ноги;\n"))
            chance = randint(1, 100)
            hp = hp - randint(10, 15)
            print("ваш запас HP -", hp)

            if punch == 1:
                if chance > 49:
                    print("попал!")
                    hp_g = hp_g - 50
                else:
                    print("не попал :(")
            elif punch == 2:
                if chance > 19:
                    print("попал!")
                    hp_g = hp_g - 40
                else:
                    print("не попал :(")
            elif punch == 3:
                if chance > 9:
                    print("попал!")
                    hp_g = hp_g - 25
                else:
                    print("не попал :(")

            if hp_g > 0:
                print("HP гоблина - ", hp_g)
            else:
                print("HP гоблина - 0")
        elif all([hp > 0, hp_g <= 0]):
            print('Гоблин - <<Ты великолепый воин и достоин силы этого легендарного меча, он твой>>')
            weapon += 1
            break
        elif hp <= 0:
            print('КОНЕЦ ИГРЫ | ты умер')
            break

if choice == 3:
    print('Ты идёшь по старой тропинке и видешь, как шайка воров напала на старого торговца')
    print("Ты можешь забрать золото, пока разбойники избивают торговца и получить дополнительный очки.\nНо ты можешь поступить по совести и чести и помочь несчастному торговцу. ")
    print('Что ты выбирешь?\n1.\n2.')
    choice2 = int(input())
    if choice2 == 1:
        print('Ты незаметно забираешь золото и уходишь.')
        print('+1000 очков')
    if choice2 == 2:
        print("Ты решил сразиться с ворами.")
        print("⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⢀⣤⣾⣿⣿⠟⠋")
        print("⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⢀⣤⣾⣿⡿⠛⠉")
        print("⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⢀⣴⣾⣿⠿⠋⠁")
        print("⠄⠄⠄⠄⠄⠄⠄⢀⣴⣾⡿⠟⠋")
        print("⠄⠄⠄⡀⢾⣶⣾⡿⠛⠁")
        print("⠄⣴⣿⣷⡘⢿⡇⠄⣠⣤⣤⣦⡀")
        print("⠸⣿⣿⣿⠁⠄⢠⣾⣿⣿⣿⣿⣿⣧")
        print("⠄⣿⣿⣿⠄⠄⣿⣿⣿⣿⣿⣿⣿⡿")
        print("⢠⣿⣿⣿⡄⢰⣿⣿⣿⣧⣌⣉⣈⣡")
        print("⢈⣿⣿⣿⣷⣿⣿⣿⣿⣿⣿⣿⣿⠟⠄⠄⠄⠄⠄⠄⠄⣤⡀")
        print("⠄⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣶⣶⣦⣀⠄⣼⣿⡇")
        print("⠄⠄⠉⠛⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⡦")
        print("⠄⠄⠄⠄⠸⣿⣿⣿⣿⣿⣿⣿⣿⡿⡿⣿⡿⠿⠛⠛⠛⠛⠁")
        print("⠄⠄⣀⡀⢶⣦⣙⠛⣛⡛⠿⠛⣩⣴")
        print("⢠⣿⣿⣿⣦⣙⠻⢿⣿⣿⣿⠿⢋⣡⣾⣶⡄")
        print("⠘⣿⣿⣿⣿⣿⠇⣼⡏⢿⡆⢺⣿⣿⣿⣿⣧")
        print("⠄⠈⣿⣿⣿⡇⠈⠛⠄⠘⠋⠄⢿⣿⣿⣿⣿⣦⣀⡀")
        print("⠰⣾⣿⣿⣿⠇⠄⠄⠄⠄⠄⠄⠄⠄⠙⠿⣿⣿⣿⣿⡇")
        print("⠄⠈⠛⠉⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠙⠛⠛⠛⠁")

        hp = 100
        hp_v = 100
        from random import *
        print("Разбоники заметили вас и самый сильный из них решил с вами сразиться")
        print(f"HP стража - {hp_v}")
        print()
        while True:
                if all([hp > 0, hp_v > 0]):
                    punch = int(
                    input("выберите место для удара:\n      1) голова; \n      2) туловище; \n      1) ноги;\n"))
                    chance = randint(1, 100)
                    hp = hp - randint(10, 15)
                    print("ваш запас HP -", hp)
                    if punch == 1:
                        if chance > 49:
                            print("попал!")
                            hp_v = hp_v - 50
                        else:
                            print("не попал :(")
                    elif punch == 2:
                        if chance > 19:
                            print("попал!")
                            hp_v = hp_v - 40
                        else:
                            print("не попал :(")
                    elif punch == 3:
                        if chance > 9:
                            print("попал!")
                            hp_v = hp_v - 25
                        else:
                            print("не попал :(")
                    if hp_v > 0:
                        print("HP стража - ", hp_v)
                    else:
                        print("HP стража - 0")
                elif all([hp > 0, hp_v <= 0]):
                    print('Ты убил одного из воров, а остальный разбежались в страхе')
                    amul += 0
                    break
                elif hp <= 0:
                    print('КОНЕЦ ИГРЫ | ты умер')
                    break







