with open('text.txt', encoding='UTF-8') as file:
    a = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    text = file.readlines()
    for i in text:
        for g in range(len(a)):
            if a[g] in i:
                print(i)
