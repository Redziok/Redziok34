def nwyraz(a1,n,q):
    return print (a1 * q**(n-1))
def sumawyraz(a1,n,q):
    if(q==1):
        return print (a1*n)
    elif(q!=1):
        return print (a1 * ( (1 - q**n) / (1 - q) ) )