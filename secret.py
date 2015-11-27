def find_message(text):
	secret = ' '
	for ele in text:
		if ele.isupper() == True:
			secret= secret + ele 
	return secret


print find_message("How are you? Eh, ok. Low or Lower? Ohhh.")
# == "HELLO", "hello"
print find_message("hello world!")
#== "", "Nothing"
print find_message("HELLO WORLD!!!")
# == "HELLOWORLD", "Capitals"
