#https://leetcode.com/problems/search-in-rotated-sorted-array-ii/description/

# case where this code will fail  arr = [1,0,1,1,1] t = 0 

def Optimal_approach(nums, target):
    n = len(nums)
    left = 0 
    right = n-1 
    
    while left <= right:
        mid = (left + right)//2 
        if nums[mid] == target :
            return True
        if nums[left] == nums[mid] == nums[right]:
            left = left + 1 
            right = right - 1 
            continue 

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
    return False 
arr =  [1,0,1,1,1] # t=0 #[4,5,6,7,0,1,2] t = 3 #[4,5,6,7,0,1,2,3] t = 0
ans = Optimal_approach(arr, 0)
print(ans)
