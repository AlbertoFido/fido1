def godos(padre, listago):
	elegidos=""
	if padre == "Jose Carlos":
		for ele in listago:
			if ele.upper()[0:1] == "W":
				elegidos += ele
				elegidos
	if padre == "Mari Carmen":
		for ele in listago:
			if ele.upper()[0:1] == "A":
				elegidos += ele
	return elegidos
print godos("Mari Carmen", {"Agila", "Amalarico, ", "Wamba, ", "Witiza"})
print godos("Jose Carlos", {"Agila", "Amalarico, ", "Wamba, ", "Witiza"})
