memo = []
def minimaBilletera(a, b):
    if(a == None and b == None): 
        return None
    elif(b == None): return a
    elif(a == None): return b
    
    if(a[0] == b[0]):
        if a[1] < b[1]: return a
        else:           return b
    if(a[0] > b[0]):
        return a
    else:
        return b 
    
def dpBilletera(B, valor): 
    memo = [[None for _ in range(valor + 1)] for _ in range(len(B))]
    def billetera(B, i, j):
        
        if(i >= len(B) and j[0] > 0):
            return None
        if(j[0] <= 0):
            return j

        if(memo[i][(j)[0]]):
            return memo[i][j[0]]
        else:
            memo[i][j[0]] = minimaBilletera(billetera(B, i+1, (j[0],j[1])), billetera(B, i+1, (j[0]-B[i], j[1]+1)))

        return memo[i][(j)[0]]
    return billetera(B,0,(valor, 0))

print(dpBilletera([2,4,4,5,5,6,7], 10))

  
