#!/usr/bin/env python
#-*- coding: utf-8 -*-

def checkio(array):
	par=[]
	sun=0
	if len(array) == 0:
		last = 0
	for ele in array:
		if array.index(ele) %2==0:
			par.append(ele)			 
	for es in par:
		sun = sun + es			
		last = sun * array[len(array)-1]			
				
	return last
li= [-37,-36,-19,-99,29,20,3,-7,-64,84,36,62,26,-76,55,-24,84,49,-65,41] #1968
print li
print checkio(li)
l1= [0,1,2,3,4,5]
print l1

print checkio(l1)

#len(li)-1
