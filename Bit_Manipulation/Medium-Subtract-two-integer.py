

x = -12
y = -5 

while y != 0:
    borrow = (~x) & y 

    x = x ^ y 

    y = borrow << 1 

print(x)