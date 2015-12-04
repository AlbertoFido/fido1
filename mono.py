def count_words(text, words):
	re=0
	for ele in words:
		if ele.upper() in text.upper(): 		
			re+=1
			
	return re



   
print count_words("How aresjfhdskfhskd you?", {"how", "are", "you", "hello"})
#== 3, "Example"
print count_words("Bananas, give me bananas!!!", {"banana", "bananas"})
#== 2, "BANANAS!"
print count_words("Lorem ipsum dolor sit amet, consectetuer adipiscing elit.",{"sum", "hamlet", "infinity", "anything"})
#== 1, "Weird text"
#b= set() conjunto vacio
