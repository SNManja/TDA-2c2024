import math


def indiceEspejo(arr):
    def indiceEspejoRec(arr, i, j):
        if(j<i):
            return False
        if(i==j):
            return arr[i] == i+1
        
        mid = i + math.floor((j-i)/2)
        if(arr[mid] == mid+1):
            return True
        elif(arr[mid] > mid+1):
            return indiceEspejoRec(arr,i,mid) 
        else:
            return indiceEspejoRec(arr,mid+1,j)
        
    return indiceEspejoRec(arr, 0,len(arr)-1)

ejemplo = [-4, -1, 2, 4, 7]


"""
    Por teorema maestro T(n) = T(n/2) + O(1) 
    a = 1 ; b = 2 
    n^(log_b a) = n^0 = 1
    2ndo caso tetha(n^0 * log n) => tetha(log n) caso 2 teorema maestro      
""" 