#!/usr/bin/env phyton 
#-*- coding: utf-8 -*-

a = int(raw_input("¿Que edad tengo?: "))

edad=23
while edad != a: 
	print " ni de coña" 
	a = int(raw_input("otra vez: "))
if edad == a:
		print "!As acertado¡"
