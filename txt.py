with open('text.txt', encoding='UTF-8') as file:

    text = file.read()
    print(text)
    cnt = text.count(" ") + text.count(".")
    print("Слов в этом текстовом документе: ",cnt)

