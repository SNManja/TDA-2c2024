'''
Este creo que es un caso particular
porque voy a dar uso a la memo con el unico fin de 
verificar si ya calcule el caso
Esto va a hacer que lo unico que me interesa es si el array da true
Si el array da true ya pase por ahi
'''

# ! El problema de esto es que pense todo como para que me devuelva si es posible o no
# ! Pero como hago cuando quiero que la output sea una lista?!?!?!
# ! Tener la lista como argumento creo que va a reventar el espacio
 

def OperacionesSeq(v,w):
    resuelve = [[None for _ in range(w+1)] for _ in range(len(v))]
    
    def OperacionesSeqRec(i, val):
        if(val > w):
            return False
        if(i == len(v) and val != w):
            return False
        if(val == w):
            return i == len(v)
        if(resuelve[i][val]):
            return False
        else:
            casoS = OperacionesSeqRec(i+1,val+v[i])
            casoM = OperacionesSeqRec(i+1,val*v[i])
            casoP = OperacionesSeqRec(i+1,val**v[i])
            
            resuelve[i][val] = casoS or casoM or casoP
        return resuelve[i][val]
    OperacionesSeqRec(0,0)
    #print(resuelve)
    res = []
    calcRes = v[0]
    for i in range(1,len(v)):
        isOutOfRange = (calcRes + v[i]) > w
        casoS = (not isOutOfRange) and resuelve[i][calcRes + v[i]]
        if(casoS):
            print("+", v[i])
            res.append("+")
            calcRes += v[i]
            continue
        isOutOfRange = calcRes * v[i] > w
        casoM = (not isOutOfRange) and resuelve[i][calcRes * v[i]]
        if(casoM):
            print("*", v[i])
            res.append("*")
            calcRes = calcRes * v[i] 
            continue
        isOutOfRange = calcRes ** v[i] > w
        casoP = (not isOutOfRange) and resuelve[i][calcRes ** v[i]]
        if(casoP):
            print("^", v[i])
            res.append("^")
            calcRes = calcRes ** v[i]
            continue
        if(not casoM and not casoP and not casoS):
            print("todo falso")
    return res        
    
    
    
    
      
