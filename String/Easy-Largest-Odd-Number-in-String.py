
"""
Input: num = "52"
Output: "5"
Explanation: The only non-empty substrings are "5", "2", and "52". "5" is the only odd number.

"""
def LargestOdd_Number(s):
    odd = 0
    num = int(s)
    if num % 2 !=0:
        return str(num)
    while num:
        n = num %10
        print(n)
        if n % 2 != 0:
            temp = n
            if odd < temp:
                odd = temp 
        num = num // 10
    if odd == 0:
        return "Zero" 
    else:
        return str(odd)

ans = LargestOdd_Number("35428")
print(ans, "ans")

print(15 % 10)