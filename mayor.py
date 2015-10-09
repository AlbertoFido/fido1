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

bucle = True
numeros = []
while bucle:
	a= int(raw_input("Introduce un numero: "))
	numeros.append(a)
	if a == 0: 
		bucle = False 
		
print " el mayor es: ", mayor(numeros) 
		


