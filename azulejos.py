def alicatar(r):
	entero=0
	cacho=0
	n=str(r)
	arriba=r
	abajo=r
	for i in range(1,int(r)+1):
		print i
		abajo=(r**2-i**2)**0.5
		print abajo
		entero+= int(abajo)
		print entero
		for p in n:
			if p == ".":
				n1=n.split(".")
				for ele in n1[1]:
					if ele >0:
						numero=int(n1[0])
						arriba=numero+1
			else:
				arriba=r
		cacho+=int(arriba)-int(abajo)
		arriba= abajo
	if int(r) != r:
		b2=str(abajo)
		for p2 in b2:
			if p2 == ".":
				n2=b2.split(".")
				for ele2 in n2[1]:
					if ele2 >0:
						numero2=int(n2[0])
						abajo=numero2+1
			else:
				abajo=abajo
		cacho += int(abajo)*2
	return [4*entero, 4*cacho]

print alicatar(2)
print alicatar(3)
print alicatar(2.1)
print alicatar(2.5)

