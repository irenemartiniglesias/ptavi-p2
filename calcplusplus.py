#!/usr/bin/python3
# -*- coding: utf-8 -*

import sys
import csv
from calcplus import resultado_fichero

if __name__=="__main__":
	fichero = sys.argv[1]
	fich = open(fichero)
	resultado_fichero(fich)
