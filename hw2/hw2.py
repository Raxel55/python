print('Введите что-угодно через пробел. Повторения слов исключатся:')
myinput = input().split()
print(' '.join(set(myinput)))