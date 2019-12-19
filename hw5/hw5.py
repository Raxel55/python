print('Введите целые положительные числа')
int_list = input().split()
for i in range(len(int_list)):
    if (int_list[i].isdigit()):
        int_list[i] = int(int_list[i])
    else:
        print("Вы ввели нецелое число")
        break
if len(int_list) != 0:
    for i in range(1, int(max(int_list)) + 2):
        if i not in int_list:
            print(i)
            break
