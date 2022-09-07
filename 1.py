str = input()
counter = 0
for i in range(len(str)-2):
    if str.lower()[i] == str.lower()[i+1] and str.lower()[i] == str.lower()[i+2]:
        counter += 1
        print(str.lower()[i], end=' ')
print(f'Количество троек: {counter}')