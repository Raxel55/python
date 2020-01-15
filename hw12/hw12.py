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


print(fib(1))
print(fib(2))
print(fib(3))
print(fib(4))
print(fib(5))