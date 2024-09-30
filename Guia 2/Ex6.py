"""
Dado un arbol binario cualquiera, disenar un algoritmo de dividir y conquistar que devuelva la maxima
distancia entre dos nodos (es decir, maxima cantidad de ejes a atravesar). El algoritmo no debe hacer recorridos
innecesarios sobre el arbol. Hint: para saber el camino mas largo de un arbol, posiblemente necesite conocer
mas que solo los caminos mas largos de sus subarboles.    
"""

from binarytree import Node

root = Node(1)
root.left = Node(2)
root.left.left = Node(3)
root.left.left.left = Node(4)
root.left.left.left.right = Node(5)

root.left.right = Node(6)
root.left.right.left = Node(7)
root.left.right.left.right = Node(8)

root.right = Node(9)


def caminoMasLargo(root):
    maximo = 0
    def recCaminoMasLargo(thisRoot):
        nonlocal maximo
        if(thisRoot is None):
            return 0
        else:
            caminoIzq =  recCaminoMasLargo(thisRoot.left)
            caminoDer =  recCaminoMasLargo(thisRoot.right)
            unionAmbos = caminoIzq + caminoDer + 1
            if(unionAmbos > maximo):
                maximo = unionAmbos
            if(caminoIzq >= caminoDer):
                return caminoIzq + 1
            else: 
                return caminoDer + 1
    recCaminoMasLargo(root)
    return maximo

print(root)
print(caminoMasLargo(root))