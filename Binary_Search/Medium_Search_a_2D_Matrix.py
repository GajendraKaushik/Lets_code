# problem : https://leetcode.com/problems/search-a-2d-matrix/description/ 

# Brute force approach itrate over the 2D array using for loop then find the target. 

#better approach using for loop and bs on

def Binary_Search(nums, target):
    n = len(nums)
    left = 0
    right = n - 1  
    
    if (n == 1) and (nums[0] == target ):
        return True
    else:
        return False
    
    while left <= right:
        print("inside bs")
        mid = (left + right)//2

        if nums[mid] == target:
            return True
        elif nums[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return False 

def Better_approach(nums, target):

    n = len(nums)
    m = len(nums[0])
    print(n ,m)

    for i in range(n):
        print( nums[i][0], "inside for,",nums[i][m - 1])
        if (nums[i][0] <= target) and (target <= nums[i][m - 1]):
            print("inside for if ")
            return  Binary_Search(nums[i], target)
    return False

arr = [[1,3,5,7],[10,11,16,20],[23,30,34,60]] #t= 3 
ans = Better_approach(arr, 3)
print(ans)
    


