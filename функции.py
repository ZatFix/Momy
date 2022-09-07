# def sell(goods, price):
#     result = goods * price
#     print(f"Товаров можно продать на {result} монет")
# sell(int(input()), int(input()))

# def equate(a, b):
#     result = (a+4*b)*(a-3*b)+a
#     print(result)
# equate(5, 3)


# def smallest(a, b, c):
#     if a < b and a < c:
#         print(a)
#     elif b < a and b < c:
#         print(b)
#     elif c < a and c < b:
#         print(c)
# smallest(3, 2, 6)

# def rotate_items(sequence):
#     sequence = [*sequence[2:], *sequence[:2]]
#     print(sequence)
#     return sequence
#
#
# rotate_items([1, 2, 3, 4, 5])


def exam(limit, *marks):
    cnt = 0
    for i in range(len(marks)):


        if marks[i] >= limit:
            cnt += 1
    print(cnt)
    return exam()
exam(3, [1, 2, 3, 4])
