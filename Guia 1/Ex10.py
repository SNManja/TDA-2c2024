'''
Tenemos cajas numeradas de 1 a N, todas de iguales dimensiones. Queremos encontrar la máxima
cantidad de cajas que pueden apilarse en una única pila cumpliendo que:
sólo puede haber una caja apoyada directamente sobre otra;
las cajas de la pila deben estar ordenadas crecientemente por número, de abajo para arriba;
cada caja i tiene un peso wi y un soporte si, y el peso total de las cajas que están arriba de
otra no debe exceder el soporte de esa otra.
Si tenemos los pesos w = [19,7,5,6,1] y los soportes s = [15,13,7,8,2] (la caja 1 tiene peso 19
y soporte 15, la caja 2 tiene peso 7 y soporte 13, etc.), entonces la respuesta es 4. Por ejemplo,
pueden apilarse de la forma 1-2-3-5 o 1-2-4-5 (donde la izquierda es más abajo), entre otras
opciones.
'''

'''
b) En hoja
'''
# !Ayuda
'''
c) Esta implementacion toma una complejidad espacial de la memo de O(max(S)*n) siendo n la cantidad de cajas
   La complejidad temporal es algo mas complejo (jeje)
   Se que los casos que haya una coincidencia  no se va a repetir el calculo
   Esto se da cuando coinciden indice y soporte.
   Ahora esto va a mejorar el algoritmo dependiendo que tan comun sea esto
   hay una relacion entre que tan larga es la secuencia y el soporte maximo a aparecer
   A su vez de estar condenado por la aleatoriedad misma de la input a ser brindada
   
   Tambien no tengo idea como abordar el bottom up?
'''

def PilaCauta(w,s):
    guardianes = [None for _ in range(len(w))]
    lvl = 0
    indices = [None for _ in range(len(w))]
    
    #
    def PCRec(sop, i):
        if (i>=len(w) or (sop and sop < 0)):
            return 0
        elif(sop == None):
            return max(PCRec(s[i],i+1)+1,PCRec(None, i+1))
        else:
            return max(PCRec(min(s[i],sop-w[i]),i+1)+1, PCRec(sop, i+1))
    return PCRec(None, 0)
        
def PilaCautaMEMO(w,s):
    guardianes = [None for _ in range(len(w))]
    lvl = 0
    indices = [None for _ in range(len(w))]
    
    memo = [[None for _ in range(max(s)+1)] for _ in range(len(w))]
    def PCRec(sop, i):
        
        if (i>=len(w) or (sop and sop < 0)):
            return 0
        elif(sop == None):
            return max(PCRec(s[i],i+1)+1,PCRec(None, i+1))
        elif(memo[i][sop] != None):
            return memo[i][sop]
        else:
            memo[i][sop] = max(PCRec(min(s[i],sop-w[i]),i+1)+1, PCRec(sop, i+1))
        return memo[i][sop]
    return PCRec(None, 0)

import time

ejemplo1 = ([100,2,3,4,23,19,7,5,6,1],[20,100,2,3,15,2,13,7,8,2])
ejemplo2 = ([50, 23, 70, 48, 32, 58, 63, 9, 34, 47, 21, 99, 66, 75, 54, 88, 57, 33, 92, 4, 15, 82, 40, 6, 74, 41, 30, 17, 53, 64, 19, 24, 29, 98, 2, 35, 96, 26, 83, 28, 12, 14, 91, 10, 20, 5, 38, 37, 67, 76, 31, 59, 93, 11, 18, 85, 61, 43, 78, 44, 81, 100, 8, 87, 52, 72, 56, 49, 60, 22, 45, 13, 71, 68, 16, 90, 77, 42, 25, 62, 97, 73, 55, 94, 3, 46, 95, 36, 27, 84, 7, 39, 51, 86, 65, 79, 89, 80, 1, 70],
            [67, 51, 76, 62, 58, 95, 38, 42, 64, 37, 41, 71, 33, 47, 85, 53, 25, 81, 83, 60, 30, 34, 55, 88, 28, 56, 79, 50, 91, 35, 29, 66, 78, 61, 20, 40, 43, 87, 39, 22, 54, 31, 77, 24, 74, 32, 21, 26, 36, 69, 19, 92, 63, 49, 75, 70, 59, 27, 57, 46, 84, 73, 52, 65, 68, 48, 18, 45, 16, 72, 44, 89, 23, 13, 12, 10, 8, 17, 3, 15, 4, 14, 9, 5, 7, 2, 6, 11, 93, 98, 82, 86, 97, 99, 100, 96, 80, 1, 6, 50])

inicio1 = time.time()

print(PilaCauta(ejemplo2[0],ejemplo2[1]))

fin1 = time.time()
print(fin1-inicio1)

inicio2 = time.time()

print(PilaCautaMEMO(ejemplo2[0],ejemplo2[1]))

fin2 = time.time()
print(fin2-inicio2)