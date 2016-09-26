#!/usr/bin/python3
# -*- coding: utf-8 -*

import csv
from calcplus import resultado_fichero


if __name__=="__main__":

	with open('fichero') as mifichero:
		lineas = csv.reader(mifichero)
		for linea in lineas:
			print(linea)
