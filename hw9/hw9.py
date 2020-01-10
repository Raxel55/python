# problem 40
d = ''.join([str(x) for x in range(200000)])
res = 1
for i in [10**x for x in range(7)]:
	res*= int(d[i])
print(res)

# problem 48
print( str(sum([x**x for x in range(1,1001)]))[-10:])


