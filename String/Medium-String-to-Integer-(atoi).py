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

ans = MyAtoi("words and 987")
print(ans)
        

