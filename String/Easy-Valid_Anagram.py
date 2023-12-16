s = "anagram"
t = "nagaram"
def BruteForce_approach(s, t):
    #if both the strings are not of same lenth then it is not a palindrome
    if len(s) == len(t):
        return False
    # Sort both the Strings
    tarr = sorted(t)
    sarr = sorted(s)
    ans = 1 
    #comapaire Both arrays elements if not same return False
    for i in range(len(tarr)):
        if tarr[i] != sarr[i]:
            ans = -1
            break


s1 = "rat"
t1 = "car"

# using map 
def Better_approach(s, t):
    #if both the strings are not of same lenth then it is not a palindrome
    if len(s) == len(t):
        mapS = {}
        # counting occurence of each word and storing it into map 
        for i in s:
            if i in mapS:
                mapS[i] += 1
            else:
                mapS[i] = 1
        # compaining it wiht seond word 
        for i in t:
            if i in mapS:
                mapS[i] -= 1
        # finaly checking the if any non zero word 
        for i in s:
            if mapS[i] != 0:
                return False
        return True
    else:
        return False 
    
print(Better_approach(s1,t1))

# count(i) return how many time i is present in the word 
def Optimal_approach(s, t):
    if len(s) == len(t):
        for i in s:
            if s.count(i) != t.count(i):
                return False
        return True
    return False

print(Optimal_approach(s1,t1))

