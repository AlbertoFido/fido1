def checkio(data):
	bo=False
	contador=0
	for ele in data:
		contador += 1
		if contador >= 10:
			for nu in data:
				if nu.isdigit():
					for may in data:
						if may.isupper():
							for mi in data:
								if mi.islower():
									bo= True
	return bo





print checkio('A1213pokl')
# == False, "1st example"
print checkio('bAse730onE4')
#== True, "2nd example"
print checkio('asasasasasasasaas')
# == False, "3rd example"
print checkio('QWERTYqwerty')
# == False, "4th example"
print checkio('123456123456')
# == False, "5th example"
print checkio('QwErTy911poqqqq')
#== True, "6th example"
