#Problem : https://leetcode.com/problems/search-a-2d-matrix-ii/

def Binary_Search(nums, target):
    n = len(nums)
    left = 0
    right = len(nums)-1

    while left <= right:
         mid = (left + right)//2
         if nums[mid] == target:
             return target
         elif nums[mid] > target:
             right = mid - 1
         else:
             left = mid + 1
    return False 

def Brute_approach(matrix, target):
    n = len(matrix)
    m = len(matrix[0])
    print(n,m)
    for i in range(n):
        ans = Binary_Search(matrix[i], target)
        if ans == target:
            return ans
    return False
        
# matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
# print(Brute_approach(matrix, 5))


## optimal approach

def Optimal_approach(matrix, target):
    n = len(matrix)
    m = len(matrix[0])
    # here we are traversing in the row and column manner --| in this manner 
    row = 0
    col = m-1 
     
    while row < n and col >=0:
        if matrix[row][col] == target:
            return True
        # target is greater then we will move on row else move on column 
        elif matrix[row][col] < target:
            row = row + 1 
            
        else:
            col = col - 1  
    return False

matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
print(Optimal_approach(matrix, 19))
 

        