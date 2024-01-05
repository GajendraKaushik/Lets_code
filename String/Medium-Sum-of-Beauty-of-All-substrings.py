#https://leetcode.com/problems/sum-of-beauty-of-all-substrings/description


# function to count the beauty of each sub string 
def countBeauty(arr):
    maxfreq = -1
    minfreq = 1e9
    print(arr)
    for i in range(len(arr)):

        # get the max frequent char from the arr
        maxfreq = max(maxfreq, arr[i])

        # get the min frequent char from the arr and min frequency should be >=1
        if arr[i] >= 1:
            minfreq = min(minfreq, arr[i])
    
    # return the difference most frequent and least frequent char or beatuty 
    return maxfreq - minfreq 

def all_substrings(s):
    res = 0
    for i in range(len(s)):

        # storing the frequency of each element 
        countfreq = [0]*26  
        for j in range(i, len(s)):
            countfreq[ord(s[j]) - ord("a")] += 1
            res += countBeauty(countfreq)
    return res 
# "aabcb"
ans = all_substrings("aabcbaa")
print(ans)



### Optimal approavh 

def beautySum(self, s: str) -> int:
    
    beauty=0
    for i in range(len(s)-2):
        Freq={}
        for j in range(i,len(s)):
            Freq.setdefault(s[j],0)
            Freq[s[j]]+=1
            beauty+=max(Freq.values())-min(Freq.values())
    return beauty
