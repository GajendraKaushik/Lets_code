# GCD(12,24) = GCD(24-12, 24)


def GCDorHFC(a,b):
    if a == 0:
        print(b)
        return b
    if b == 0: 
        print(a)
        return a
    if a > b:
        ans = GCDorHFC(abs(a-b), b)
    else:
        ans = GCDorHFC(abs(b-a), a)
    return ans 

# a = GCDorHFC(12,28)
# print(a)

def GCDorHFC_Modulo(a,b):
    while(a > 0 and b>0):
        if a > b:
            a = a % b
        else:
            b = b % a
    if a == 0:
        return b
    else:
        return a  
    

a = GCDorHFC_Modulo(12,28) 
print(a)