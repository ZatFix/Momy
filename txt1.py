with open('text.txt', encoding='UTF-8') as file:
    text = file.readlines()
with open('file.txt', 'a', encoding='UTF-8') as file:
    st = input('Какую строку хотиет записать?')
    for i in text:
        if st in i:
            x = input('Это строка уже есть. Вы хотите записать её ещё раз')
            if x.lower() == 'да':
                st = '\n' + st
                file.write(st)
            else:
                break