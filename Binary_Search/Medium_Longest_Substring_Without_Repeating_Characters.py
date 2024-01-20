# Problem Statement   :  https://leetcode.com/problems/longest-substring-without-repeating-characters/description/ 

# Better approcah  using hash set time complexity O(2n)
def find_longest_sub_string_without_repiting(s):
    max_len = 0
    l = 0
    r = 0 
    n = len(s)
    chek_set = set()
    while r< n:
        if s[r] not in chek_set:
            chek_set.add(s[r])
            temp = r - l + 1 
            if max_len < temp:
                max_len = temp
            r = r+1 
        else:
            chek_set.remove(s[l])
            l = l + 1 
    return max_len


# Optimal approach using map time complexity O(n)
def Optimal_approach(s):
    max_len = 0
    l = 0
    r = 0 
    n = len(s)
    chek_set = {}
    while r< n:
        if s[r] in chek_set:
            l = max(chek_set[s[r]] +1, l)
       
        chek_set[s[r]] = r
        temp = r - l + 1 
        max_len = max(max_len, temp)
        r = r+1
    return max_len

s = "abcabb"
s1 ="bbbbb"
s3  ="pwwkew"
# ans = find_longest_sub_string_without_repiting(s3)
# print(ans)
ans1 = Optimal_approach(s3)
print(ans1)

