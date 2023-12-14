# Problem = https://leetcode.com/problems/single-element-in-a-sorted-array/description/

"""
You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once.

Return the single element that appears only once.

Your solution must run in O(log n) time and O(1) space.

Example 1:

Input: nums = [1,1,2,3,3,4,4,8,8]
Output: 2
Example 2:

Input: nums = [3,3,7,7,10,11,11]
Output: 10

""" 

#Brute Force approach using traversing the Array 

def Brute_approach(nums):
    n = len(nums)

    # if there is only one element in the array
    if n == 1:
        return nums[0]
    
    for i in range(n):
        # check for first element in the array 
        if i == 0:
            if nums[i] != nums[i+1]:
                return nums[i] 
        
        # check for last element in the array 
        elif i == n-1:
            if nums[n-2] != nums[n-1]:
                return nums[n-1]
        else:
            # for single element its prev and next element will not be equals
            if nums[i] != nums[i-1] and nums[i] != nums[i+1]:
                return nums[i]
    
# arr = [3,3,7,7,10,11,11] #[1,1,2,3,3,4,4,8,8]
# print(Brute_approach(arr))

def Optimal_approach_using_BS(nums):
    n = len(nums)
    if n == 1 :
        return nums[0]
    
    # tream down the search space so that we will have less conditions 
    left = 1
    right = n-2

    # check for first element in the array 
    if nums[left] != nums[0]:
        return nums[0]
    
    # check for last element in the array 
    elif nums[right] != nums[n-1]:
        return nums[n-1]
    
    while left <= right :
        mid = (left + right) //2 

        # if mid element is single element 
        if nums[mid] != nums[mid-1] and nums[mid] != nums[mid+1]:
            return nums[mid]
        
        # desiding element is in left half or right half based on index is even or odd
        if ((mid%2 == 1 and nums[mid-1] == nums[mid] ) or (mid % 2 == 0 and nums[mid] == nums[mid+1] )):
            left = mid + 1
        else:
            right = mid - 1 

     #(even, odd)(index) --> eleement is on right half
     #(odd, even) --> element is on left half 

arr = [1,1,2,3,3,4,4,8,8]
print(Optimal_approach_using_BS(arr))                                                     
    