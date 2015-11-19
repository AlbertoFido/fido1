#!/usr/bin/env python
#-*- coding: utf-8 -*-

def checkio(array):
	par=[]
	for ele in array:
		if array.index(ele) %2==0:
			par.append(ele)
			last = par *(len(li)-1)			
				
	return last
li= [1,3,5]
print li
print checkio(li)


#len(li)-1
