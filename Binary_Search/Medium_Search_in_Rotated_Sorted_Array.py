# https://leetcode.com/problems/search-in-rotated-sorted-array/description/

#------- Navi approach ----- # 
# def swap(nums, start , end):
#     temp = nums[start]
#     nums[start] = nums[end]
#     nums[end] = temp 

# def My_approach(nums):
#     small_index = float('-inf')
#     n = len(nums)
#     for i in range(n-1):
#         if nums[i] > nums[i+1]:
#             small_index = i + 1 
#             break
#     print(small_index)
#     for i in range((n-small_index)):
#         swap(nums, i , small_index)
#         print(small_index, i)
#         small_index += 1
        
#     print(nums)

# arr = [4,5,6,7,0,1,2]
# My_approach(arr)

# --------------- linear search is a brute force approach ------------ #

#------------- Optimal approach using BS ---------------# 
# case where this code will fail  arr = [1,0,1,1,1] t = 0 

def Optimal_approach(nums, target):
    n = len(nums)
    left = 0 
    right = n-1 
    
    while left <= right:
        mid = (left + right)//2 
        
        if nums[mid] == target :
            return mid
        
        if nums[left] <= nums[mid]:

            if nums[left] <= target and target <= nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if nums[mid] <= target and target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
    return -1 
arr = [4,5,6,7,0,1,2] #[4,5,6,7,0,1,2,3]
ans = Optimal_approach(arr, 3)
print(ans)
print(arr[ans])
