def astroTrade(P):
    
    memo = [[None for _ in range(len(P))] for _ in range(len(P))]
    def astroVoid(P, i, c):
        
        if(c<0 or c>len(P)):
            return -9999999999
        elif(i == len(P)):
            return 0
        else:
            
            if(c >0 ):
                memo[i][c] = max(astroVoid(P,i+1,c), astroVoid(P, i+1, c+1) - P[i], astroVoid(P, i+1, c-1) + P[i])
            else:
                memo[i][c] = max(astroVoid(P,i+1,c), astroVoid(P, i+1, c+1) - P[i])
        return memo[i][c]
            
    return astroVoid(P,0,0)

test1 = [1,2,3,4,5]
test2 = [1,2,3,50]
test3 = [20,123,12,400,10,1,1,1,1]
test4 = [3,2,5,6]
test5 = [3,6,10]

print(astroTrade(test1))

print(astroTrade(test2))

print(astroTrade(test3))

print(astroTrade(test4)) # 6

print(astroTrade(test5)) # 7
