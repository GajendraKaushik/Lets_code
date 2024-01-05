#https://leetcode.com/problems/longest-palindromic-substring/

def isPalindrom(s):
    reversed = s[::-1]
    print(reversed)
    if s== reversed:
        return len(s)
    return 0
# print(isPalindrom("aba"))

def Longest_Pailindrom(s):
    ans =""
    maxLen = 0
    for i in range(0, len(s)):
        temp = ""
        for j in range(i, len(s)):
            temp += s[j]
            print(temp)
            count = isPalindrom(temp)
            if maxLen < count :
                maxLen = count
                ans = temp
    return ans

ans = Longest_Pailindrom("a")
print(ans)
