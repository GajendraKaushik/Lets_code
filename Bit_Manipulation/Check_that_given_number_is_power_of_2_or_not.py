"""
8 = (1000)2
8-1 = 7 = (0111)2 
n & n-1 = (1000) & (0111) = 0 
"""

def power_2(n):
    if n & n-1:
        return True
    return False

n = 18 
ans = power_2(18)
print(ans)