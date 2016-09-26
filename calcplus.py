#!/usr/bin/python3
# -*- coding: utf-8 -*

import sys
import calcoohija


def resultado_operaciones(lineas):
	for linea in lineas:
		linea_operacion= linea.split(",")
		operando = linea_operacion[0]
		resultado_final = float(linea_operacion[1])
		for i in range(len(linea_operacion)-2):
			num_añade = float(linea_operacion[i+2])
			resultado_final= calcoohija.resultado(operando, resultado_final, num_añade)	
	print(resultado_final)
	

def lineas_fichero(lines):
	for line in lines:
		lineas =line.split()
		total = resultado_operaciones(lineas)


def resultado_fichero(fich):
	lines =fich.readlines()
	lineas_fichero(lines)
	
if __name__== "__main__":
	fichero = sys.argv[1]
	documento = open(fichero)
	resultado_fichero(documento)
	documento.close()


			
			
			
		


