# https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses/description/

"""
Input: s = "(1+(2*3)+((8)/4))+1"
Output: 3
Explanation: Digit 8 is inside of 3 nested parentheses in the string.

"""
def Max_Nesting_Depth(s):
    count = 0
    temp = 0
    for c in s:
        if c == '(':
            temp += 1
            if temp > count :
                count = temp
        if c == ')':
            temp -= 1
            # if temp > count :
            #     count = temp 
    return count

s = "(1+(2*3)+((8)/4))+1"
s1 = "(1)+((2))+(((3)))"

ans = Max_Nesting_Depth(s)
print(ans)


  
            
        

    