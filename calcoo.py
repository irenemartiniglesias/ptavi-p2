#!/usr/bin/python3
# -*- coding: utf-8 -*

import sys


class Calculadora():


    def plus(self, op1, op2):
        return op1 + op2 
        
    def minus(self, op1, op2):
        return op1 - op2
        

def result(operacion, op1, op2):
    if (operacion == "suma"):
        total = Calculadora().plus(op1, op2)
    elif (operacion == "resta"):
        total = Calculadora().minus(op1,op2)
    else:
        sys.exit("Error: the operation is incorrect")
    return total
    

if __name__ == "__main__":

    try:
        op1 = float(sys.argv[1])
        operacion = sys.argv[2]
        op2 = float(sys.argv[3])
    except ValueError:
        sys.exit("Error: Non numerical parameters")
    print(result(operacion,op1,op2))
