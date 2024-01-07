# https://leetcode.com/problems/string-to-integer-atoi/description/

def MyAtoi(s):
    res = 0
    temp = s.strip()
    sing = 1
    p = 0
    if temp[0] == "-":
        sing = -1
        p = 1
        temp = temp[1:]
        print(temp)
    for i in temp:
        a = ord(i) - ord('0')
        if a in range(0, 10):
            res = res * 10 + a
    return res * sing

# ans = MyAtoi("words and 987")
# print(ans)


def MyAtoi_2(s):
    res = 0
    sign = 1
    digits = "0123456789"
    s = s.strip()
    if s and (s[0] == "-" or s[0] == "+"):
        if s[0] == "-":
            sign = -1
            s = s[1:]
        elif s[0] == "+": 
            sign = +1
            s = s[1:]
        
    for char in s:
        if char in digits:
            res = res * 10 + int(char)
        else:
            break
    res *= sign
    IntMax = 2**31 - 1
    IntMin = -2**31
    res = max(IntMin, min(IntMax, res))
    return res

ans = MyAtoi_2("words and 987")
print(ans)
    

