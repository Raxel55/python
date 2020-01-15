# Рекурсия
# def kollats(n, acc=0):
#     if n == 1:
#         return acc
#     elif n % 2 == 0:
#         return kollats(n / 2, acc + 1)
#     else:
#         return kollats(3 * n + 1, acc + 1)
#
#
# n = input('Введите натуральное число: ')
# if n.isdecimal() and n != '0':
#     print(kollats(int(n)))
# else:
#     print('Вы ввели либо не натуральное число, либо 0')


# Цикл
n = input('Введите натуральное число: ')
if n.isdecimal() and n != '0':
    n = int(n)
    i = 0
    while n != 1:
        if n % 2 == 0:
            n /= 2
        else:
            n = 3 * n + 1
        i += 1
    print(i)
else:
    print('Вы ввели либо не натуральное число, либо 0')
