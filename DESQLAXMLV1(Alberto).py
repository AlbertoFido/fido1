#!/usr/bin/env python
#-*- coding: utf-8 -*-
#---------------------------------------------------------------#
#Migrar la informacion de una tabla de oracle a un documento XML#
#---------------------------------------------------------------#

#Importamos la liberias necesarias para el ejercicio
import cx_Oracle as dbapi
import sys

#creamos el fichero que vamos a editar
f= open (sys.argv[1], "w")

#Conectamos a la base de datos
SE= dbapi.connect("SE/se@localhost")

#Le damos a una variable el resultado de la consulta SQL
cur = SE.cursor()
cur.execute("""select * from ALUMNOS""")
par = SE.cursor()
par.execute("""select COLUMN_NAME from USER_TAB_COLUMNS where TABLE_NAME = 'ALUMNOS' """)

#Comenzamos el script...
lista=[]
f.write("<TABLA_ALUMNOS>")
f.write('\n')
f.write("Tabla de alumnos en xml")
f.write('\n')
for ele in par:
	lista+=ele
for con in cur:
		f.write("<"+lista[0]+">")
		f.write(str(con[0]))
		f.write("</"+lista[0]+">")
		f.write('\n')
		f.write("<"+lista[1]+">")
		f.write(con[1])
		f.write("</"+lista[1]+">")
		f.write('\n')
		f.write("<"+lista[2]+">")
		f.write(str(con[2]))
		f.write("</"+lista[2]+">")
		f.write('\n')
f.write("</TABLA_ALUMNOS>")
	
	
f.close()
#'\n'=retorno de carro(intro)
#r=leer
#r+=leer y modificar
#w=modificar o crear
#varaible.write(linea) = escribir linea en la variable
#variable.readlines()= leer lineas en la variable
