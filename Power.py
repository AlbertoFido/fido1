#!/usr/bin/env python
#-*- coding: utf-8 -*-


def index_power(array, n):
	if len(array) > n:
		resultado = array[n]**n	
	else:
		resultado= -1
	return resultado

print index_power([1,1,1,1,1,1,1,1,1,1], 9)
 #== 9, "Square"
print index_power([1, 3, 10, 100], 3)
 #== 1000000, "Cube"
print index_power([0, 1], 0)
 #== 1, "Zero power"
print index_power([1, 2], 3)
 #== -1, "IndexError"
