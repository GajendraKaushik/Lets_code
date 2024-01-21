# problem stetment : https://leetcode.com/problems/count-good-numbers/description/ 

"""
A digit string is good if the digits (0-indexed) at even indices are even and the digits at odd indices are prime (2, 3, 5, or 7).

For example, "2582" is good because the digits (2 and 8) at even positions are even and the digits (5 and 2) at odd positions are prime. However, "3245" is not good because 3 is at an even index but is not even.
Given an integer n, return the total number of good digit strings of length n. Since the answer may be large, return it modulo 109 + 7.

A digit string is a string consisting of digits 0 through 9 that may contain leading zeros.
""" 
# solution approach 

"""
> first of all we need to calculate how many odd and even number is present in the range of 0 to 9.
> then we need to calculate the odd and even position in 4 lenght numbers 0,1,2,3,4 so there is 3 even positions and 2 odd position is present 
> formula to calculate odd and evne lenth positions 
   odd : n / 2 number of odd posions 
   even : (n/2 + n% 2 ) number of even positions 

using above approach we can solve the problem 
"""
def Power(n, y):
    M = 1000000007
    if y == 1:
        return n 
    p = Power(n, y//2)
    p *= p
    p %= M
    if y % 2 :
        p *= n
        p %= M
    return p  
    
def Count_good_Number(n):
    M = 1000000007
    odd = n // 2
    even = (n// 2) + (n % 2) 
    good =  (Power(5,even) * Power(4,odd) ) % M 
    return good


ans = Count_good_Number(50)
print(Power(5,2))
print(ans)


# Better approach 

def countGoodNumbers(self, n: int) -> int:
    ans = 1 
    rem = n %  2 
    n -= rem 
    ans = pow(20, n//2, 10**9 + 7)
    if rem == 1:
        ans *= 5
    return ans% (10**9 + 7)