class fecha:
	def __init__(self, f1):
		self.f=f1
	def mostrar(self):
		return self.f
d=1
date= fecha(raw_input ("introduce una fecha:"))
if d == 1:
	print date.mostrar()
