"""
Problem : 
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:

Input: n = 1
Output: ["()"]
"""


def BackeTrack_approach(n):
    ans = [] 
    def BackTrack(open, close, curr_str):
        if len(curr_str) == n*2:
            ans.append(curr_str)
            return  
        if open < n:
            BackTrack(open + 1, close, curr_str +"(")
        
        if close < open :  
            BackTrack(open, close + 1, curr_str +")")
    BackTrack(0, 0, "")
    return ans 
    
n = 3 
ans = BackeTrack_approach(3)
print(ans)


