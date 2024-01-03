"""
Example 1:
Input: N = 12345
Output: 5
Explanation: N has 5 digits

"""
import math
def CountDigit(n):
    count = 0 
    while n:
        n = n//10
        count += 1
    print(count)

CountDigit(12345)

# Better approach 

def CountDigitB(n):
    temp =str(n)
    print(len(temp)) 

CountDigitB(12345)

# optimal approach 

def CountDigitO(n):
    digit = math.floor(math.log10(n) + 1)
    print(digit)

CountDigitO(123456)
