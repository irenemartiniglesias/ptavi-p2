#!/usr/bin/python3
# -*- coding: utf-8 -*

# Vamos a crear una calculadora que herede de la Clase Calculadora

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
        resultado = CalculadoraHija().plus(op1, op2)
    elif (operacion == "resta"):
        resultado = CalculadoraHija().minus(op1,op2)
    elif (operacion == "multiplica"):
        resultado = CalculadoraHija().multiply(op1,op2)
    elif (operacion == "divide"):
        resultado = CalculadoraHija().divide(op1,op2)
    else:
        sys.exit("Error: the operation is incorrect")
    return resultado


if __name__ == "__main__":

    try:
        op1 = float(sys.argv[1])
        operacion = sys.argv[2]
        op2 = float(sys.argv[3])
    except ValueError:
        sys.exit("Error: Non numerical parameters")
    print(resultado(operacion,op1,op2))
	

