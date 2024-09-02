import time

import numpy as np

# Primera matriz: valores entre 0 y 100
matriz1 = np.random.randint(-100, 101, size=(100, 100))
'''
Hay un terreno, que podemos pensarlo como una grilla de m filas y n columnas, con trampas
y pociones. Queremos llegar de la esquina superior izquierda hasta la inferior derecha, y desde
cada casilla sólo podemos movernos a la casilla de la derecha o a la de abajo. Cada casilla i,j
tiene un número entero Ai,j que nos modificará el nivel de vida sumándonos el número Ai,j (si
es negativo, nos va a restar |Ai,j | de vida). Queremos saber el mínimo nivel de vida con el que
debemos comenzar tal que haya un camino posible de modo que en todo momento nuestro nivel
de vida sea al menos 1. Por ejemplo, si tenemos la grilla
'''

'''
Pensar algoritmo de backtracking
1. Tengo 2 movimientos posibles, abajo o derecha
2. Si se pasa el rango de la matriz float(-inf)
3. A lo largo que avanzo en la recursion tengo que guardar 2 valores, minimo de vida para llegar ahi y vida actual
3,5. ! para la memo: En cada valor guardar la vida actual comenzando de 0 y el minimo de vida en el camino a llegar ahi

'''


def travesia(A):
    m = len(A) - 1 
    n = len(A[0])-1
    def travesiaRec(A,i,j):
        if(i == 0 and j == 0):
            return A[i][j]
        if(i < 0 or j < 0 or i > m or j > n):
            return float('+inf')
        
        thisCost = A[i][j]
        return min(travesiaRec(A,i,j-1) + thisCost, travesiaRec(A,i-1,j) + thisCost)
        
    
    return 1 - travesiaRec(A,m,n) # Le agrego 1 porque pense que tenia que tener 1 de vida



def travesiaDP(A):
    m = len(A) - 1 
    n = len(A[0])-1
    memo = [[None for _ in range(n+1)] for _ in range(m+1)]
    def travesiaRec(A,i,j):
        
        if(memo[i][j] is not None):
            return memo[i][j]
        
        if(i == 0 and j == 0):
            return A[i][j]
        if(i < 0 or j < 0 or i > m or j > n):
            return float('+inf')
        
        thisCost = A[i][j]
        memo[i][j] = min(travesiaRec(A,i,j-1) + thisCost, travesiaRec(A,i-1,j) + thisCost)
        
        return memo[i][j]
        
    
    return 1 - travesiaRec(A,m,n) # Le agrego 1 porque pense que tenia que tener 1 de vida




inicio = time.time()

#print(travesia(matriz1))


fin = time.time()
#print(fin-inicio)

inicio1 = time.time()

print(travesiaDP(matriz1))


fin1 = time.time()
print(fin1-inicio1)

#Podemos ver que en casos grandes el algoritmo directamente llena el stack cuando la matriz es lo suficientemente grande
#Pero con DP este mismo algoritmo va a los chapazos y ademas no revienta el stack