#!/usr/bin/env python
#-*- coding: utf-8 -*-

def count(matriz, fila, columna):
	contador = 0
	
	sonvecinos = ((-1,-1),(-1, 0),(-1, 1), (0, -1),(0, 1),(1, -1), (1, 0), (1, 1))
	
	for vecino in sonvecinos:
		if columna+vecino[1]>=0 and fila+vecino[0]>=0 and columna+vecino[1]<=len(matriz) and fila+vecino[0]<=len(matriz):
			contador = contador + matriz[fila+vecino[0]][columna+vecino[1]]	
	return contador


matriz = ((1, 0, 0, 1, 0),
		  (0, 1, 0, 0, 0),
		  (0, 0, 1, 0, 1),
		  (1, 0, 0, 0, 0),
		  (0, 0, 1, 0, 0),)
fila = 1
columna= 2

print count (matriz, fila, columna)














matriz = ((1, 0, 0, 1, 0),
		  (0, 1, 0, 0, 0),
		  (0, 0, 1, 0, 1),
		  (1, 0, 0, 0, 0),
		  (0, 0, 1, 0, 0),)
fila = 1
columna= 2
