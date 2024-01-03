# https://leetcode.com/problems/roman-to-integer/description/

RomanDict = {
"I":1, 
"V":5, 
"X":10, 
"L":50, 
"C":100, 
"D":500, 
"M":1000
}

def Rom_To_Integer(s):
    num = 0
    temp = RomanDict.get(s[0])

    for key in s:

        if temp < RomanDict.get(key):
            num -= temp 
            num += RomanDict.get(key) - temp
        else:
            num += RomanDict.get(key)
        
        temp = RomanDict.get(key)
    return num

ans = Rom_To_Integer("IVIII")
print(ans)