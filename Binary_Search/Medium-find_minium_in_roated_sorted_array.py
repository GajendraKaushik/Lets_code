def Optimal_approach(nums):
    low = 0
    high = len(nums) - 1
    ans = float('inf')

    while low <= high:
        mid = (low + high) // 2
 
        if nums[low] <= nums[high]:
            ans = min(ans, nums[low])
            break
            
        if nums[low] <= nums[mid]: 
            ans = min(ans, nums[low])  
            low = mid + 1  
 
        else:  
            ans = min(ans, nums[mid])  
            high = mid - 1  
  
    return ans

arr = [3,4,5,1,2] #[4,5,6,7,0,1,2,3]
print(Optimal_approach(arr))