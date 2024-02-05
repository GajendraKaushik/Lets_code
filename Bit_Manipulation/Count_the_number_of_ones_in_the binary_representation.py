"""
https://www.hackerearth.com/practice/basic-programming/bit-manipulation/basics-of-bit-manipulation/tutorial/ 
"""
def countOne(n):
    count = 0
    while n :
        n = n & (n-1)
        count += 1
    return count

n = 10
ans = countOne(n)
print(ans)