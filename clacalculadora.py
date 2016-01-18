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
bo = True
while bo == True:
	operacion = calculadora (int (raw_input ("introduce un numero:")), int (raw_input ("introducir Otro:"))) 
	opera= raw_input("indica operacion o pulsa c para salir (+,-,*,/): ")
	if opera == "+":
		operacion.sumar()
	elif opera == "-":
		operaciom.restar()
	elif opera == "*":
		operacion.multiplicar()
	elif opera == "/":
		operacion.dividir()
	elif opera == "c":
		print "adios"
		bo= False
	else:
		print "error de operacion"


