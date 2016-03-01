#!/usr/bin/env python
#-*- coding: utf-8 -*-
class coche:
	"""Abstraccion de los objetos coche"""
	def __init__(self, diesel):
		self.combustible = diesel
		self.color= "rojo"
	def arrancar(self):
		if self.combustible > 0:
			print "arranca"
		else:
			print "no arranca"
	def conducir(self):
		if self.combustible >0:
			self.combustible -= 1
			print "Quedan", self.combustible, "litros"
		else:
			print "no se mueve"

peito=coche(3)
