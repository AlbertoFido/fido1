def left_join(phrases):
	lis= list(phrases)
	re=[]
	contador=0
	for ele in lis:
		if ele == "right":
			contador=lis.index(ele)
			lis[contador]="left"
			re = lis
	buscar="right"
	remplazar="left"
	cadena=",".join(lis)
	re =cadena.replace(buscar, remplazar)
	
		
	return re


print left_join(("left", "right", "left", "stop"))
#== "left,left,left,stop", "All to left"
print left_join(("bright aright", "ok"))
#== "bleft aleft,ok", "Bright Left"
print left_join(("brightness wright",))
#== "bleftness wleft", "One phrase"
print left_join(("enough", "jokes"))
#== "enough,jokes", "Nothing to replace"
