import math


class ErrorPersonalizado(Exception):
    def __init__(self, mensaje, codigo_error=101):
        super().__init__(mensaje)
        self.codigo_error = codigo_error

def res(arr):
    memo = [[None for _ in range(len(arr))] for _ in range(len(arr))]
    def suma(arr,i,j):
        if(memo[i][j] is not None):
            return memo[i][j]
        
        mid = i+ math.floor((j-i)/2)
        
        if i == j:  # Un solo elemento
            memo[i][j] = arr[i]
        else:
            mid = i + (j - i) // 2
            memo[i][j] = suma(arr, i, mid) + suma(arr, mid + 1, j)
        
        return memo[i][j]
            
    def masALaIzq(arr, i, j):   
        if(i == j or j < i):
            return True
        elif(i+1==j):
            return (arr[i]>arr[j])
        elif((j-i+1) % 2 == 1): #El +1 es pq empieza a contar del 0
            raise ErrorPersonalizado( f" ({i},{j}) El tamaño del subarreglo no es potencia de 2.", 101)
        else:
            mid = i+ math.floor((j-i)/2)
            sumaIzq = suma(arr,i,mid)
            sumaDer = suma(arr,mid+1,j)
            if(sumaIzq <= sumaDer):
                return False
            else:
                return masALaIzq(arr,i,mid) and masALaIzq(arr,mid+1,j)
        
    return masALaIzq(arr,0,len(arr)-1)
    
    res = masALaIzq(arr, 0, len(arr)-1)
    return res
