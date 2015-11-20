#!/usr/bin/env python
#-*- coding: utf-8 -*-

def checkio(array):
	sun=0
	if len(array) != 0:
		for i in range(0, len(array)):
			if i%2 == 0:
				sun += array[i]
		print sun		
		last = sun * array[-1]			
				
	return last
li= [-37,-36,-19,-99,29,20,3,-7,-64,84,36,62,26,-76,55,-24,84,49,-65,41] #1968
print li
print checkio(li)
l1= [0,1,2,3,4,5]
print l1
print checkio(l1)
		
				

		

#len(li)-1
