def dodawanie(a1,b1,a2,b2):
    if(b1+b2>0):
        return print(str(a1+a2) + '+' + str(b1+b2) + 'i')
    elif(b1+b2<0):
        return print(str(a1+a2) + '' + str(b1+b2) + 'i')
    else:
        return print(str(a1+a2))
def odejmowanie(a1,b1,a2,b2):
    if(b1-b2>0):
        return print(str(a1-a2) + '+' + str(b1-b2) + 'i')
    elif(b1-b2<0):
        return print(str(a1-a2) + '' + str(b1-b2) + 'i')
    else:
        return print(str(a1-a2))