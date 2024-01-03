"""
Example 1:
Input: n = 36
Output: 1 2 3 4 6 9 12 18 36
Explanation: All the divisors of 36 are printed.
"""
def allDevisors(n):
    listDiv = []
    mid = n//2
    for item in range(1, mid+1):
        if n % item == 0:
            listDiv.append(item)
    listDiv.append(n)
    print(listDiv)

allDevisors(97)