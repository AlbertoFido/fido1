#!/usr/bin/env python
#-*- coding: utf-8 -*-

def count(matriz, fila, columna):
	contador = 0
	
	if matriz[fila -1][columna -1] == 1:
		contador+=1
	if matriz[fila -1][columna] == 1:
		contador+=1
	if matriz[fila][columna -1] == 1:
		contador+=1
	if matriz[fila -1][columna +1] == 1:
		contador+=1
	if matriz[fila ][columna +1] == 1:
		contador+=1
	if matriz[fila +1][columna +1] == 1:
		contador+=1
	if matriz[fila +1][columna ] == 1:
		contador+=1
	if matriz[fila +1][columna -1] == 1:
		contador+=1
	return contador

matriz = ((1, 0, 0, 1, 0),
		  (0, 1, 0, 0, 0),
		  (0, 0, 1, 0, 1),
		  (1, 0, 0, 0, 0),
		  (0, 0, 1, 0, 0),)
fila = 1
columna= 2
		 
#mapa = len(matriz) #esa variable cuenta las filas de la matriz 
	
print count (matriz, fila, columna)
