def checkio(number):
	resultado= int(1)
	cad=str(number)
	for ele in cad:
		if ele != "0":
			resultado *=int(ele)
		
			
			
			
			
	

	return resultado


print checkio(123405)
# == 120
print checkio(999)
# == 729
print checkio(1000)
# == 1
print checkio(1111)
# == 1
