#!/usr/bin/env python
#-*- coding: utf-8 -*-

#def count(matriz, fila, columna):
	#X_max= len(grid[row])-1
	#Y_max= len(grid) -1
			
 #   return vecino
matriz = ((1, 0, 0, 1, 0),
          (0, 1, 0, 0, 0),
          (0, 0, 1, 0, 1),
          (1, 0, 0, 0, 0),
          (0, 0, 1, 0, 0),)
fila = 2
columna = 2  
#mapa = len(matriz) #esa variable cuenta las filas de la matriz 
print matriz[0]
print matriz[1]
print matriz[2]
print matriz[3]
print matriz[4]
cor= matriz[fila][columna]
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
print contador
	
	
	
