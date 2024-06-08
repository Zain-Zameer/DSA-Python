def compundProfit(p,r,n):
    total = 0
    if(n==0):
        return int(p)
    else:
        p = p+ (p*r/100) 
        return compundProfit(p,r,n-1) 

print(compundProfit(10000,10,5))