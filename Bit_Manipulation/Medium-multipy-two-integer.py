def multipy(a,b):
    res = 0
    while b != 0:
        if b & 1:
            res += a
        a <<=1
        b >>= 1 
    return res 

ans = multipy(12,5)

print(ans)
