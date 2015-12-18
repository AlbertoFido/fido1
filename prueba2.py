#!/usr/bin/env phyton 
#-*- coding: utf-8 -*-

a = int(raw_input("¿Que edad tengo?: "))

edad=23
while edad != a:
	if a > edad:
		print "tan viejo no soy" 
		a = int(raw_input("otra vez: "))
	elif a < edad:
		print " gracias por el cumplido pero soy mas viejo "
		a=int(raw_input("prueba otra vez: "))
	else:
		print "nos vemos"
if edad == a:
		print "!As acertado¡"
