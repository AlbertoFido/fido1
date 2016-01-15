#!/usr/bin/env python
#-*- coding: utf-8 -*-
class calculadora:
	"""abstracion del objeto calculadora"""
	def __init__(self,op1,op2):
		self.a=op1
		self.b=op2
	def sumar(self):
		s=self.a+self.b
		print s
	def restar(self):
		r=self.a-self.b
		print r
	def multiplicar(self):
		m=self.a*self.b
		print m
	def dividir(self):
		d=self.a//self.b
		print d

operacion=calculadora(int(raw_input("introduce un numero: ")),int(raw_input("introduce otro: ")))
