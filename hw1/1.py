print("Соответствия между объектами разных классов")
print("Проверка int == bool")
print("1 == True :", 1 == True)
print("0 == True :", 0 == True)
print("-1 == True :", -1 == True)
print("2 == True :", 2 == True)
print("-0 == True :", -0 == True)

print("\nПроверка str == bool")
print("'1' == True :", '1' == True)
print("'0' == True :", '0' == True)
print("'' == True :", '' == True)
print("'True' == True :", 'True' == True)
print("'False' == True :", 'False' == True)

print("\nПроверка str == int")
print("'1' == 1 :", '1' == 1)
print("'0' == 0 :", '0' == 0)
print("'' == 0 :", '' == 0)
print("'a' == 97 :", 'a' == 97)
print("'1' == 49 :", '1' == 49)
print("'1' == chr(49) :", '1' == chr(49))