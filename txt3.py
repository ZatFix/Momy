with open("events.txt", "a", encoding='UTF-8') as file:
    a = 0
    while a <= 20:
        a = str(a)
        file.write(a)
        file.write(" ")
        a = int(a)
        a += 2