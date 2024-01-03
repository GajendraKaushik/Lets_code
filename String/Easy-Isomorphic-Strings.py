#https://leetcode.com/problems/isomorphic-strings/description/

from collections import Counter
def isIsomorphic(str1, str2):
    if len(str1) != len(str2):
        return False
    return [*map(s.index, s)] == [*map(t.index, t)]
s = "egg"
t = "add"
ans = isIsomorphic(s,t)
print(ans)


def isIsomorphic_2(s, t):
    map1 = []
    map2 = []
    for idx in s:
        map1.append(s.index(idx))
        print(map1)
    for idx in t:
        map2.append(t.index(idx))
        print(map2)
    if map1 == map2:
        return True
    return False
print(isIsomorphic_2(s,t))