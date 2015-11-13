#!/usr/bin/env python
#-*- coding: utf-8 -*-
def checkio(listaprueba):
	datar = []
	dic={}
	for ele in listaprueba:
		if ele in dic:
			dic[ele] += 1
		else:
			dic[ele]=1
	for ele in listaprueba:
		if dic[ele] > 1:
			datar.append(ele)
	return datar
listaprueba=[1, 2, 30, 30, 6, 6, 5]
print listaprueba
print checkio(listaprueba) 

 

