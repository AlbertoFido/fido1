def left_join(phrases):
	li= list(phrases)
	re=""
	contador=0
	for ele in li:
		if ele == "right" :
			li[contador] == "left"
			re = li
		contador +=1
		else:
			re = "error"
   
	return re


print left_join(("left", "right", "left", "stop"))
#== "left,left,left,stop", "All to left"
print left_join(("bright aright", "ok"))
#== "bleft aleft,ok", "Bright Left"
print left_join(("brightness wright",))
#== "bleftness wleft", "One phrase"
print left_join(("enough", "jokes"))
#== "enough,jokes", "Nothing to replace"
