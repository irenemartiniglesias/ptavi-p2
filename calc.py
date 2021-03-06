#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys


def plus(op1, op2):
    """ Function to sum the operands """
    return op1 + op2


def minus(op1, op2):
    """ Function to substract the operands """
    return op1 - op2


def multiply(op1, op2):
    """ Funcion para multiplicar los operandos"""
    return op1 * op2


def divide(op1, op2):
    """Funcion para dividir los operandos"""
    return op1 / op2

if __name__ == "__main__":

    try:
        operando1 = int(sys.argv[1])
        operando2 = int(sys.argv[3])
    except ValueError:
        sys.exit("Error: Non numerical parameters")

    if sys.argv[2] == "suma":
        solucion = plus(operando1, operando2)
    elif sys.argv[2] == "resta":
        solucion = minus(operando1, operando2)
    elif sys.argv[2] == "multiplica":
        solucion = multiply(operando1, operando2)
    elif sys.argv[2] == "divide":
        solucion = divide(operando1, operando2)
    else:
        sys.exit("Error: the operation is incorrect")

    print(solucion)
