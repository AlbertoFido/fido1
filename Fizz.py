#!/usr/bin/env python
#-*- coding: utf-8 -*-

def checkio(number):
	salida = " "
	if number % 3 != 0 and number % 5 != 0:
		salida = str(number)
	elif number % 3 == 0 and number % 5 == 0:
		salida = "Fizz Buzz"
	elif number % 3 == 0:
		salida = "Fizz"
	elif number % 5 == 0:
		salida = "Buzz"
	return salida
	

print checkio(15) 
#== "Fizz Buzz", "15 is divisible by 3 and 5"
print checkio(6)
#= "Fizz", "6 is divisible by 3"
print checkio(5)
#== "Buzz", "5 is divisible by 5"
print checkio(7)
#== "7", "7 is not divisible by 3 or 5"
