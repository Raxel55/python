# # Вариант c целыми неотрицательными числами
# print('Введите целые неотрицательные числа')
# int_str = input()
# int_list = list()
# temp = ""
# for char in int_str:
#     if char.isdigit():
#         temp += char
#     elif temp != "":
#         int_list.append(int(temp))
#         temp = ""
# if temp != "":
#     int_list.append(int(temp))
# sum = 0
# for i in int_list:
#     sum += i
# print(sum)

# # Вариант с целыми числами 1
# print('Введите целые числа')
# int_str = input()
# int_list = list()
# temp = ""
# for i in range(len(int_str)):
#     if int_str[i].isdigit():
#         temp += int_str[i]
#     elif temp != "":
#         if (i-len(temp)-1) != -1 and int_str[i-len(temp)-1] == "-":
#             temp = "-" + temp
#         int_list.append(int(temp))
#         temp = ""
# else:
#     if int_str[- len(temp) - 1] == "-":
#         temp = "-" + temp
#     if temp != "" and temp != "-":
#         int_list.append(int(temp))
# sum = 0
# for i in int_list:
#     sum += i
# print(sum)

# Вариант c целыми числами 2
print('Введите целые числа')
int_str = input()
int_list = list()
temp = ""
for char in int_str:
    if char.isdigit():
        temp += char
    elif temp != "":
        if temp != "-":
            int_list.append(int(temp))
        temp = ""
    if char == "-" and temp == "":
        temp = "-"
if temp != "" and temp != "-":
    int_list.append(int(temp))

sum = 0
for i in int_list:
    sum += i
print(sum)
