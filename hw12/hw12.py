# Рекурсия
# def fib(n):
#     if n in (1,2):
#         return 1
#     return fib(n-1) + fib(n-2)

# Цикл
def fib(n):
    a, b = 1, 1
    for i in range(n-2):
        a, b = b, b + a
    return b


for j in range(1,9):
    print(fib(j))

