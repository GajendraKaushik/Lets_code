
def add(a, b):
    # max 32 bit number in python 
    mask = 0xffffffff

    while (mask & b):
        a, b = a ^ b, (a & b ) << 1

    return (mask & a) if b > 0 else a 

ans = add(3,-7) 

print(ans)