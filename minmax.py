def checkio(*args):
	dif = 0
	if len(args) > 0:
		dif = max(args)-min(args)
	return dif



print checkio(1, 2, 3)
#, "3-1=2"
print checkio(5, -5)
#, "5-(-5)=10"
print checkio(10.2, -2.2, 0, 1.1, 0.5)
#, "10.2-(-2.2)=12.4"
print checkio()
#, "Empty"
