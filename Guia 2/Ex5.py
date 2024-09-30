"""
Ejercicio 5 (PotenciaSum) ⋆
Suponga que se tiene un metodo potencia que, dada un matriz cuadrada A de orden 4 x 4 y un numero n,
computa la matriz An. Dada una matriz cuadrada A de orden 4 x 4 y un numero natural n que es potencia de 2 
(i.e., n = 2k para algun k ≥ 1), desarrollar, utilizando la tecnica de dividir y conquistar y el metodo potencia,
un algoritmo que permita calcular

A^1 + A^2 + ... + A^n

Procure que el algoritmo propuesto aplique el metodo potencia, sume y haga productos de matrices una cantidad
estrictamente menor que O(n) veces.
    
"""
def PotenciaSum(matriz):
    
def multMatriz(a,b):
    res = [[None for _ in range(len(a))] for _ in range(len(b))]
    for i in range(len(a)):
        newElem = 1
        for j in range(len(b)):
            newElem = 