# Problem : https://leetcode.com/problems/find-peak-element/


def Brute_approach(nums):
    n = len(nums)
    for i in range(n):
        if ((i==0 or nums[i]> nums[i+1] ) and (i == n-1 or nums[i] > nums[i-1])):
            return i

# arr =  [1,2,1,3,5,6,4] 
# print(Brute_approach(arr))

# Optimal approach using Binary Search 

def Optimal_approach(nums):
    n = len(nums)
    
    # only one element is array 
    if n == 1 :
        return 0
    
    # if first element is peak element  
    elif nums[0 ] > nums[1]: return 0 

    # if last element is peak element
    elif nums[n-1] > nums[n-2] : return n-1 

    left = 1
    right  = n-2 
    while left <= right:
        mid = (left + right)//2 

        # condition for peak element 
        if nums[mid] > nums[mid-1] and nums[mid] > nums[mid+1]:
            return mid
        
        #eleminating the increasing left half 
        elif nums[mid] > nums[mid-1]:
            left = mid + 1

        # eleminating the right half
        elif nums[mid] < nums[mid+1]:
            right = mid - 1

        # special condition for reverse of peal element 
        else:
            left = mid + 1
    return -1   

arr =  [1,2]#[1,5,1,2,1]#[1,2,1,3,5,6,4] 
print(Optimal_approach(arr))



