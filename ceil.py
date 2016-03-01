def ceeil(num):
	nuevo=0
	n=str(num)
	n1=n.split(".")
	print n1
	for ele in n1[1]:
		if ele >0:
			numero=int(n1[0])
			nuevo=numero+1
	return nuevo

print ceeil(100.01)
print ceeil(2.5)
