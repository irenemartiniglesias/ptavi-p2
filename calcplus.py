#!/usr/bin/python3
# -*- coding: utf-8 -*

import sys

class Calculadora():
	def plus(self, op1, op2):
		return op1 + op2
	def minus(self, op1, op2):
		return op1 - op2

class CalculadoraHija(Calculadora):
	def multiply(self, op1, op2):
		return op1 * op2
	def divide(self, op1, op2):
		try:
			return op1 / op2
		except ZeroDivisionError:
			sys.exit("Division by zero is not allowed")

def resultado(operacion, op1, op2):
	if (operacion == "suma"):
		total = CalculadoraHija().plus(op1, op2)
	elif (operacion == "resta"):
		total = CalculadoraHija().minus(op1,op2)
	elif (operacion == "multiplica"):
		total = CalculadoraHija().multiply(op1,op2)
	elif (operacion == "divide"):
		total = CalculadoraHija().divide(op1,op2)
	else:
		sys.exit("Error: the operation is incorrect")
	return total
	
def resultado_operaciones(lineas):
	for linea in lineas:
		linea_operacion= linea.split(",")
		operando = linea_operacion[0]
		resultado_final = float(linea_operacion[1])
		for i in range(len(linea_operacion)-2):
			num_añade = float(linea_operacion[i+2])
			resultado_final= resultado(operando, resultado_final, num_añade)	
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
	fich = open(fichero)
	resultado_fichero(fich)
	fich.close()


			
			
			
		


