"""
Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

 

Example 1:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
Example 2:

Input: nums = [0,1]
Output: [[0,1],[1,0]]
Example 3:

Input: nums = [1]
Output: [[1]]
 
"""


def recurPerpute(nums, ds, ans, freq):
    # if ds length is equal to nums len then we will append the copy of ds not ds reference 
    if len(ds) == len(nums):
        ans.append(ds.copy())
        return ds
    
    for i in range(len(nums)):
        # if for that element in freq list 0 is marked then only we will append that in ds 
        if not freq[i]:
            ds.append(nums[i])
            freq[i] = 1
            recurPerpute(nums, ds, ans, freq)

            # after return we will pop the element from the ds list 
            freq[i] = 0
            ds.pop(len(ds) - 1)


def Bettor_approach(nums):
    ans = []
    ds = []
    freq =[0]*len(nums)
    recurPerpute(nums, ds, ans, freq)
    return ans

# nums = [1,2,3]
# ans = Bettor_approach(nums)
# print(ans)


# copy approach to sole ve the proble 

def Optimal_recurPermute(nums, index, ans1):
    if index == len(nums):
        ans1.append(nums.copy())
        return
    
    for i in range(index,len(nums)):
        nums[i] , nums[index] = nums[index], nums[i]
        Optimal_recurPermute(nums, index + 1, ans1)
        nums[i] , nums[index] = nums[index], nums[i]

def Optimal_approach(nums):
    ans2 = []
    Optimal_recurPermute(nums,0,ans2)
    return ans2

nums = [1,2,3]
ans1 = Optimal_approach(nums)
print(ans1, "")










