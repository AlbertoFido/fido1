def boolean(x, y, operation):
	re = 0
	co= x and y
	di= x or y
	if x == True:
		im= y
	else:
		im= 1
	if x != y:
		ex= 1
	else:
		ex=0
	if x == y:
		eq = 1
	else:
		eq= 0
	op={"conjunction": co,"disjunction": di, "implication": im, "exclusive": ex, "equivalence": eq}
	if op[operation] == 1:
		re = 1
	else:
		re = 0		
	return re


print boolean(1, 0, "conjunction")
# == 0, "and"
print boolean(1, 0, "disjunction")
# == 1, "or"
print boolean(1, 1, "implication") 
#== 1, "material"
print boolean(0, 1, "exclusive")
# == 1, "xor"
print boolean(0, 1, "equivalence")
# == 0, "same?"
