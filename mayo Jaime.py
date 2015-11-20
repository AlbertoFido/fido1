#!/usr/bin/env python
#-*- coding: utf-8 -*-
num=[]
def mayo(num):
	mayor = 0
	for ele in num:
		if ele > mayor:
			mayor = ele
	return mayor
	
numero = int(raw_input("introduce un numero positivo(negativo si te aburres): "))
ma= numero
while numero >= 0: 
	if numero > ma: 
		num.append(numero) 
	numero = int(raw_input("introduce un numero positivo(negativo si te aburres): "))
if ma <= 0:
	print " no has introducido ningun numero" 
else:
	print "el numero mayor es: " +str(mayo(num))
