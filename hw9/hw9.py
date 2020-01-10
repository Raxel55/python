#problem 9
summa = 1000
mul = [a*b*(summa-a-b) for a in range(1, summa//3) for b in range(a+1, summa//2-a//2) if a**2+b**2 == (summa-a-b)**2]
print(mul)

#problem 6
num = 100
sub = sum([x for x in range(1, num + 1)])**2-sum([x**2 for x in range(1, num + 1)])
print(sub)
