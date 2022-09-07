# string = input('Введите строку ')
# a = string.count("А")
# a1 = string.count("а")
# b = string.count("Б")
# b2 = string.count("б")
# a3 = a + a1
# b3 = b + b2
# if a3 > b3:
#     print('A')
# elif b3 > a3:
#     print('Б')
# else:
#     print("Error")
#
#
# string = input('Введите строку ')
# string = string.lower()
#
# a = string.find('а')
# b = string.find('б')
# if a < b:
#     print("а")
# elif b < a:
#     print('b')
# else:
#     print('Error')
#
#
# string = input('Введите строку ')
# print(string.replace('а', 'ая'))
#
#
# string = input('Введите строку ')
# print(string.title())
#
#
# import random
# alf = "ёйцукенгшщзхъфывапролджэячсмитьбю"
# for i in range(5):
#     print(random.choice(alf), end='')
#     print(random.randint(0,9), end='')


# string = input('Введите строку ')
# a = string.count('(')
# b = string.count(')')
# if a == b and string.find('(') < string.find(')'):
#     print('yes')
# else:
#     print('no')


# string = input('Введите строку ')
# print(string.replace(", ", "\n"))


# string = input('Введите строку ')
# a = int(input())
# print((string + '\n') * a)

n = int(input())
for i in range(n):
    string = input('Введите строку ')

if string.find('Кот') or string.find('кот'):
    print('Мяу')

else:
    print('no')



