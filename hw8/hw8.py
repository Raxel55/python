def f():
	x = input()
	if x == 'cancel':
		print('Bye')
		return
	elif x.isdecimal() or ((x[0] == '-') and x[1:].isdecimal()):
		x = int(x)
		if x%2==0:
			x=int(x/2)
		else:
			x=x*3+1
	else:
		x = 'No number entered'
	print(x)
	return f()
f()
