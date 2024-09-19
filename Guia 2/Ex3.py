import math


def potenciaLogaritmica(a,b):
    memo = [None for _ in range(b+1)]
    def potenciaLogaritmicaRec(a,b):
        
        halfB = math.floor(b/2)
        if(b == 0):
            return 1
        if(b == 1):
            return a
        if(memo[b] is not None):
            return memo[b]        
        else:
            if(memo[halfB] is None):
                memo[halfB] = potenciaLogaritmica(a,halfB)
            if(b % 2 == 1):
                memo[b] = a * memo[halfB] * memo[halfB]
            else:
                memo[b] =  memo[halfB] * memo[halfB]
        return memo[b]
    return potenciaLogaritmicaRec(a,b)

"""
    Por teorema maestro T(n) = T(n/2) + O(1) 
    asumiendo que las operaciones de multiplicacion que se hacen al mergear son O(1)
    a = 1 ; b = 2 
    n^(log_b a) = n^0 = 1
    2ndo caso tetha(n^0 * log n) => tetha(log n) caso 2 teorema maestro      
""" 