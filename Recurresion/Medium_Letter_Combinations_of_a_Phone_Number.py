"""
Problem:  
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.
Example 1:

Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
Example 2:

Input: digits = ""
Output: []
Example 3:

Input: digits = "2"
Output: ["a","b","c"]

"""
keyboard = {
"2": "abc",
"3": "def",
"4": "ghi",
"5": "jkl",
"6": "mno",
"7": "pqrs",
"8": "tuv",
"9": "wxyz"
}

def BruteForce_approach(s):
        ans = []
        if len(digits) == 1 :
            return [i for i in keyboard[digits[0]]]
        for i in range(len(digits)):
            for j in range(i+1, len(digits)):
                for k in keyboard[digits[i]]:
                    for l in keyboard[digits[j]]:
                        ans.append(k+l)
        return ans 

digits = ""

ans = BruteForce_approach(digits)

print(ans)


def Optimal_approach(s):
    ans = []
    keyboard = {
    "2": "abc",
    "3": "def",
    "4": "ghi",
    "5": "jkl",
    "6": "mno",
    "7": "pqrs",
    "8": "tuv",
    "9": "wxyz"
    }
     
    def recursive(i, currStr):
        if len(currStr) == len(s):
            ans.append(currStr)
            return 
        for char in keyboard[s[i]]:
            recursive(i + 1 , currStr + char)
    
    if s :
        recursive(0, "")
    return ans

s = '234'
ans1 = Optimal_approach(s)
print(ans1)
     
     
     
 
