#Importante notar que si ya se corto en un intervalo, no se va a volver a cortar en el mismo

def cE(C):
    memo = [[None for _ in range(len(C))] for _ in range(len(C))]
    def valor(a,b):
        return b-a
        
    
    def cortesEconomicos(C,a,b):
        
        if(b-a <= 0): 
           return 0
        if(memo[a][b]):
            return memo[a][b]
        
        for i in range(a,b-1):           
            for j in range(i+1,b):
                
                if(j-i <= 1):
                    actual = valor(C[i], C[j])
                else:
                    print("CortesEco",  cortesEconomicos(C,i,j), valor(C[i],C[j]) )
                    actual = cortesEconomicos(C,i,j) + valor(C[i],C[j])
                
                if(memo[i][j] == None):
                    memo[i][j] = actual
               
            
        return memo[a][b]
    return cortesEconomicos(C,0,len(C))
        