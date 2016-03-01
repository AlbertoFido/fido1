#jaime.canillas@iesfernandoaguilar.es
def rayadas(palabras):
	con=0
	vocales = "A,E,I,O,U,Y"
	consonantes= "B,C,D,F,G,H,J,K,L,M,N,P,Q,R,S,T,V,W,X,Z"
	separadores=","
	for sep in separadores:
		palabra=palabras.replace(sep," ")
	words=palabra.split()
	print words
#			if ele[0].upper() in consonantes:
#				if ele[1].upper() in vocales:
#					con+=1
#			elif ele[0].upper() in vocales:
#				if ele[1].upper() in consonantes:
#					con+=1
	return con

print rayadas("My name is ...")
print rayadas("Hello Word")
print rayadas("A quantity of striped words.")
print rayadas("dog,cat,mouse,bird.human.")
