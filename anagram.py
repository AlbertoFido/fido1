def verify_anagrams(first_word, second_word):
	res=False
	dic={}
	dic2={}
	dic3={}
	for ele in first_word:
		if ele.upper() in dic:
			dic[ele.upper()] +=1
		elif ele == " ":
			dic3[ele]=1
		else:
			dic[ele.upper()]=1
	for el in second_word:
		if el.upper() in dic2:
			dic2[el.upper()] +=1
		elif el == " ":
			dic3[el]=1
		else:
			dic2[el.upper()]=1
	if dic == dic2:
		res = True
	return res

print verify_anagrams("Programming", "Gram Ring Mop")
# == True, "Gram of code"
print verify_anagrams("Hello", "Ole Oh")
# == False, "Hello! Ole Oh!"
print verify_anagrams("Kyoto", "Tokyo")
# == True, "The global warming crisis of 3002"

