#jaime.canillas@iesfernandoaguilar.es
def rayadas(texto):
	res=0
	VOCALES = "AEIOUY"
	CONSONANTES = "BCDFGHJKLMNPQRSTVWXZ"
#aqui separamos las palabras
	text=texto.replace(","," ")
	pala=text.replace("."," ")
	palabra=pala.split()
#Aqui comprobramos si las palabras son "palabras rayadas"
	for pal in palabra:
		print pal
		if len(pal)<2: continue
		i=0
		while i<len(pal)-1:
			if VOCALES.count(pal[i].upper())==0 and CONSONANTES.count(pal[i].upper())==0 or \
				VOCALES.count(pal[i].upper())==VOCALES.count(pal[i+1].upper()) or \
				CONSONANTES.count(pal[i].upper())==CONSONANTES.count(pal[i+1].upper()):
					i=len(pal)
			i+=1
			if i==len(pal)-1: 
				print i
				print len(pal)-1
				res+=1
	return res

print rayadas("My name is")
print rayadas("Hello Word")
print rayadas("A quantity of striped words.")
print rayadas("dog,cat,mouse,bird.human")
