
import sys
f= open (sys.argv[1], "r")
dicc={}
for linea in f:
	if linea[0] > 2 and linea[0].isalpha():
		for ele in linea:
			if ele == "=":
				con=linea.index(ele)
				if linea[con+1:-1].isdigit():
					dicc[linea[0:con]]=int(linea[con+1:-1])
				else:
					dicc[linea[0:con]]=linea[con+1:-1]
print dicc


f.close()
#'\n'=retorno de carro(intro)
#r=leer
#r+=leer y modificar
#w=modificar o crear
#varaible.write(linea) = escribir linea en la variable
#variable.readlines()= leer lineas en la variable
