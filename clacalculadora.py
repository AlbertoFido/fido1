class calculadora: 
	"""Abstracion del Objeto calculadora""" 
	def __init__(self, op1, op2): 
		self.a = op1 
		self.b = op2 
	def sumar(self): 
		s = self.a + self.b 
		print s 
	def restar(self): 
		r = self.a - self.b 
		print r 
	def multiplicar(self): 
		m = self.a * self.b 
		print m 
	def dividir(self):
		d =self.a // self.b
		print d
	def mayor(self):
		if self.a > self.b:
			print self.a, "es mayor que", self.b 
		elif self.a < self.b:
			print self.b, "es mayor que", self.a
		else:
			print self.a, "y", self.b, "son iguales"
	def oorr(self):
		o=self.a or self.b
		print o
	def aann(self):
		a=self.a and self.b
		print a


bo = True
operacion = calculadora (int (raw_input ("introduce un numero:")), int (raw_input ("introducir otro numero:")))
while bo == True:
	opera= raw_input("indica operacion(+, -, *, /, M para comparar o B para operar en binario), pulsa 'c' para salir o 'r' para resetear : ")
	if opera == "+":
		operacion.sumar()
	elif opera == "-":
		operacion.restar()
	elif opera == "*":
		operacion.multiplicar()
	elif opera == "/":
		operacion.dividir()
	elif opera == "m":
		operacion.mayor()
	elif opera == "b":
		operab=raw_input("Indica operacion (or, and)")
		if operab == "or":
			operacion.oorr()
		elif operab == "and":
			operacion.aann()
		else:
			print "error de operacion"
	elif opera == "c":
		print "adios ^-^"
		bo= False
	elif opera == "r":
		operacion = calculadora (int (raw_input ("introduce un numero:")), int (raw_input ("introducir otro numero:"))) 
	else:
		print "error de operacion"



