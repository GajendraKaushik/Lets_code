"""
Example 1:
Input: N = 123
Output: 321
Explanation: The reverse of 123 is 321

""" 

def Reverse_Number(n):
    print(12345)
    reverse = 0
    while n:
        reverse = reverse * 10 + n % 10
        n = n//10
    print(reverse)

Reverse_Number(12345)

def Reverse_NumberB(n):
    print(n)
    reversed = str(n)
    # print("".join(reversed(reversed)),"reversed")
    print(reversed[::-1], "::")
    print(reversed[slice(None,None, -1)],"slice")
Reverse_NumberB(12345)