"""
⋆En este ejercicio diseñamos un algoritmo para encontrar ciclos en un digrafo. Decimos que un
digrafo es acíclico cuando no tiene ciclos dirigidos. Recordar que un (di)grafo es trivial cuando
tiene un sólo vértice.
a) Demostrar con un argumento constructivo que si todos los vértices de un digrafo D tienen
grado de salida mayor a 0, entonces D tiene un ciclo.
b) Diseñar un algoritmo que permita encontrar un ciclo en un digrafo D cuyos vértices tengan todos
grado de salida mayor a 0.
c) Explicar detalladamente (sin usar código) cómo se implementa el algoritmo del inciso anterior. El algoritmo resultante tiene que tener complejidad temporal O(n + m).
d) Demostrar que un digrafo D es acíclico si y solo si D es trivial o D tiene un vértice con
dout(v) = 0 tal que D \ {v} es acíclico.
e) A partir del inciso anterior, diseñar un algoritmo que permita determinar si un grafo D
tiene ciclos. En caso negativo, el algoritmo debe retornar una lista v1, . . . , vn de vértices
tales que dout(vi) = 0 en D \ {v1, . . . , vi−1} para todo i. En caso afirmativo, el algoritmo
debe retornar un ciclo.
f) Explicar detalladamente (sin usar código) cómo se implementa el algoritmo del inciso anterior.
El algoritmo resultante tiene que tener complejidad temporal O(n + m).
"""

"""
a)
Tengo un grafo Gn que vamos a generar de a pasos.
En un principio comienzo con 2 vertices, conecto uno con el otro y como requiero que ambos tengan grado de salida > 0 
no me queda alternativa que conectar con el anterior.

Este problema lo voy a tener para todo n
Porque Asumamos que llego a conectar todos los vertices al siguiente, 

Importante tener en cuenta que hasta el momento supuestamente no hay ciclos.
Esto quiere decir que empezando de todo vertice del grafo tengo un camino que llega a un vertice final.
En caso que este vertice final este conectado a otro vertice, este otro vertice tiene que ser del grafo,
por ende no va a quedar otra que conectar este con un vertice previo en uno de los caminos
Formando un ciclo.

Esta unidireccionalidad siempre se va a dar, porque cualquier conexion que haga hacia el lado contrario formaria un ciclo.


"""

""" 
b)
Primero necesito modelar el digrafo. Voy a tomar una matriz de adyacencia. Para esto van a ser dos matrices de
tama;o nxn donde una representa la salida y otra la entrada
"""


def maxValue(aristas):
    maxVal = -1
    
    for elem in aristas:
        
        if(elem[0] > maxVal): maxVal = elem[0]
        if(elem[1] > maxVal): maxVal = elem[1]
    return maxVal

def genMatrizAdyacencia(aristas):
    # Aca asumo que se pasan aristas de valores numericos y tengo la buena fe de que el usuario va a pasar
    # vertices nombrados como numeros. Es una implementacion muy primitiva de un constructor en base a listado de aristas
    
    maxVal = maxValue(aristas)
    dIn = [[0 for _ in range(maxVal + 1)] for _ in range(maxVal + 1)]
    dOut = [[0 for _ in range(maxVal + 1)] for _ in range(maxVal + 1)]
    
    for elem in aristas:
        dOut[elem[0]][elem[1]] = 1
        dIn[elem[1]][elem[0]] = 1
    return (dOut, dIn)

testGrafo = [(0,1),(1,0),(2,0)]
matrizTestGrafo = (genMatrizAdyacencia(testGrafo))

for elem in matrizTestGrafo[0]:
    print(elem)
    
print(" ")
for elem in matrizTestGrafo[1]:
    print(elem)

#Como toda componente conexa si tienen todos los vertices una salida, va a generar un ciclo.
#Puedo tomar un vertice cualquiera y empezar a avanzar en un camino hasta volver a llegar a un vertice que pase
def b(dout):
    passed = set()
    res = [0]
    def passinThru(dout, act):
        if(act in passed):
            
            return True
        thisCase = dout[act]
        for i in range(len(thisCase)):
            if (thisCase[i] == 1):
                passed.add(i)
                res.append(i)
                return passinThru(dout, i)
        return False
    
    isOk = passinThru(dout, 0)
    if(not isOk):
        print("Algoritmo esta mal o pasaste mal el grafo salamin. Acordate que por contrato todos los vertices tienen salida")
    return res
    

print(b(matrizTestGrafo[0]))
    



