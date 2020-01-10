#problem 9
summa = 1000
mul = [a*b*(summa-a-b) for a in range(1, summa//3) for b in range(a+1, summa//2-a//2) if a**2+b**2 == (summa-a-b)**2]
print('problem 9: ' + str(mul[0]))

#problem 6
num = 100
sub = sum([x for x in range(1, num + 1)])**2-sum([x**2 for x in range(1, num + 1)])
print('problem 6: ' + str(sub))

# problem 48
print('problem 48: ' + str(sum([x**x for x in range(1,1001)]))[-10:])

# problem 40
d = ''.join([str(x) for x in range(200000)])
res = 1
for i in [10**x for x in range(7)]:
	res*= int(d[i])
print('problem 40: ' + str(res))
