#!/usr/bin/env python
#-*- coding: utf-8 -*-
#Escribe un script que reciba una lista de numeros
#de tamaño indeterminado pero no infinito por el teclado y muestre por pantalla el mayor
#Version Jaime
mayor = 0
entretenido = True
while entretenido: #mientras_que_el_usuario_no_se_aburra
	num = int(raw_input("introduce un numero positivo(negativo si te aburres): "))#pedire un numero
	if num < 0:
		entretenido = False
	elif num > mayor: #mirar si es mayo que e mayo hasta ahora
		mayor = num #si es que si tengo un nuevo mayor
	#si es que no me quedo con el que tenia
print "el mayor es: " + str(mayor) #el_mayor
