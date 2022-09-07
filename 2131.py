pupils = {}
n = int(input("кол-во учеников: "))
for i in range(n):
    stud = input().split()
    pupils[stud[0]] = stud[1:len(stud)]
for p, s in pupils.items():
    print(p, "изучает", *s)