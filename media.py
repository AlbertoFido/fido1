#!/usr/bin/env python
#-*- coding: utf-8 -*-

def mediana(li):
	li.sort()
	if len(li)%2 == 1:
		central= li[len(li)//2]
	else:
		central=(li[len(li)//2] + li[len(li)//2-1])/2.0
	return central
   
li=[1, 2, 3, 4, 5] #3
print li
print mediana(li)
li2=[3, 1, 2, 5, 3] #3
print li2
print mediana(li2)
li3=[1, 300, 2, 200, 1] # 2
print li3
print mediana (li3)
li4=[3, 6, 20, 99, 10, 15] # 12.5 
print li4
print mediana (li4)

