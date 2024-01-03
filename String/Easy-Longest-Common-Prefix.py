#Longest Common Prefix
# https://leetcode.com/problems/longest-common-prefix/description/

"""
Input: strs = ["flower","flow","flight"]
Output: "fl"

"""

def Longest_Common_Prefix_Brute(strs):
    cnt = 0
    ans =""
    for i in strs[0]:
        print(i)
        for j in strs:
            print(j)
            if j[cnt] != i:
                return ans
        ans += i
        cnt += 1


strs1 = ["flower","flow","flight"]
strs = ["dog","racecar","car"]
ans = Longest_Common_Prefix_Brute(strs)
print(ans)

def Optimal(strs):
    ans = ""
    strs = sorted(strs)
    sFirst = strs[0]
    sLast = strs[-1]
    for i in range(min(len(sFirst),len(sLast))):
        if (sFirst[i] != sLast[i]):
            return ans 
        ans += sLast[i]
        return ans 

strs1 = ["flower","flow","flight"]


