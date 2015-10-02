#!/usr/bin/env phyton 
#-*- coding: utf-8 -*-
n =int(raw_input ("Introduzca por favor un número: "))
numero = 0
while numero == 0 :
	if n % 2 == 0:
		print "par"
		numero += 1
	else:
		print "impar"
		n = int(raw_input ( " otro numero, me gustan mas los pares: "))


