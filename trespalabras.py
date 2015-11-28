def checkio(words):
	cad2=words.split(' ')
	contador=0
	salida = False
	for ele in cad2:
		if ele.isalpha():
			contador+=1
		else:
			contador = 0
		if contador >= 3:
			salida = True
	return salida

print checkio("start 5 one two three 7 end")
#True
print checkio("Hello World hello") 
#== True, "Hello"
print checkio("He is 123 man")
#== False, "123 man"
print checkio("1 2 3 4")
# == False, "Digits"
print checkio("bla bla bla bla")
# == True, "Bla Bla"
print checkio("Hi")
# == False, "Hi"
