#!/usr/bin/env python
#-*- coding: utf-8 -*-
#Escribe un script que reciba una lista de numeros
#de tamaño indeterminado pero no infinito por el teclado y muestre por pantalla el mayor
#Version Jaime
mayor = 0
num = int(raw_input("introduce un numero positivo(negativo si te aburres): "))#pedire un numero
while num >= 0: #mientras_que_el_numero_sea_mayor_que_0
	if num > mayor: #mirar si es mayor que el mayor hasta ahora
		mayor = num #si es que si tengo un nuevo mayor
	num = int(raw_input("introduce un numero positivo(negativo si te aburres): "))#pedire un numero
if mayor == 0:
	print " no has introducido ningun numero" 
else:
	print "el mayor es: " + str(mayor) #el_mayor


#Hacer un nuevo commit que muestre un mensaje cuando el usuario se aburra de primeras 
