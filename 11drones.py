#!/usr/bin/env python
#-*- coding: utf-8 -*-
def drones(amigos, uno,  otro):
	relacionados = False
	pares = []
	for cadena in amigos:
		pares.append(cadena.split('-'))
	condrones = set()
	for pareja in pares:
		condrones.add(pareja[0])
		condrones.add(pareja[1])
	dicdrones = {}
	for dron in condrones:
		dicdrones[dron] = []
	for pareja in pares:
		dicdrones[pareja[0]].append(pareja[1])
		dicdrones[pareja[1]].append(pareja[0])
	for dron in dicdrones[uno]:
		if dron == otro:
			relacionados = True
		for dronj in dicdrones[dron]:
			if dronj == otro:
				relacionados = True
	return relacionados

social_net = ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
		    "scout3-scout1", "scout1-scout4", "scout4-sscout", 
		    "sscout-super")
print drones(social_net, "scout2", "scout3")
print 'scout2 y scout3 relacionados'
print drones(social_net, "super", "scout2")
print 'super y scout2 relacionados'
print drones(social_net, "dr101", "sscout")
print 'dr101 y sscout NO relacionados'
