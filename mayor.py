#!/usr/bin/env python
#-*- coding: utf-8 -*-
#Escribe un script que reciba una lista de numeros
#de tamaño indeterminado por el teclado y muestre por pantalla el mayor

def mayor(numeros):
	num = 0
	for a in numeros:
		if a > num:
			num = a	
	return num
numeros = []

contador = 0 
while contador != 5:
	a= int(raw_input("Introduce un numero: "))
	numeros.append(a)
	contador = contador + 1 
		
print " el mayor es: ", mayor(numeros) 
		


