#pascal traingle 
# 1
# 1 2 1
# 1 3 3 1
# 1 4 6 4 1

# to solve paskel's traingle we will be using ncr formula as row n col
# to get the especific element

class Solution:
    # n = rownumber 
    def getRow_Col(self, n, c):
        result = 1
        for i in range(c):
            result = result*(n-i)
            result = result//(i+1)
        return result
obj = Solution()
ans = obj.getRow_Col(4,2)
print(ans)

# # logic to ganerate all element of specific row of pascel's traingle 
# ### brute force approach 
## time complexity O(n*c)
def getRow_Col(n, c):
        result = 1
        for i in range(c):
            result = result*(n-i)
            result = result//(i+1)
        return result
row = 3
for col in range(1, row+1):
    n = 3 # 3rd row so n-1
    ans = getRow_Col(n-1, col-1)
    print(ans, end=" ")

### optimal approach 
## time complexity O(n)
def pascal_optimal_Triangle(n):
    ans = 1 
    print(ans, end=" ") # printing 1st element

    for i in range(1, n):
         ans = ans*(n-i)
         ans = ans//i
         print(ans, end=" ")
    print()
n = 5 
pascal_optimal_Triangle(5)

## logic to print the entire pascal traingle 
## time complexity O(n*n)
def entire_pascalTriangle(n):
    ans = 1 
    print(ans, end=" ") # printing 1st element

    for i in range(1, n):
         ans = ans*(n-i)
         ans = ans//i
         print(ans, end=" ")
    print()
n = 5
for i in range(1,6):
     entire_pascalTriangle(i)



    


    
    