"""
Problem: 
Given an integer array nums of unique elements, return all possible 
subsets
 (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

 

Example 1:

Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
Example 2:

Input: nums = [0]
Output: [[],[0]]
"""

# reccursive approach 

def Power_set(nums):
    ans = [] 
    n = len(nums) 

    def reccursive(index, subArr):
        if index == n:
            ans.append(subArr.copy())
            return 
        subArr.append(nums[index])
        reccursive(index + 1, subArr)
        subArr.remove(nums[index])
        reccursive(index + 1, subArr)
    reccursive(0, [])
    return ans 

nums = [1,2,3]
ans = Power_set(nums)
print(ans)

# 95% efficient non recursive approach

def Optimal_approach(nums):
    ans = [[]]
    for num in nums:
        copy = [s.copy() for s in ans]
        for s in copy:
            print(s, "s")
            s.append(num)
            print(s, "s1")
        print(copy ,"copy")
        ans += copy 
        print(ans)
    return ans 

nums = [1,2,2]
ans1 = Optimal_approach(nums)

print(ans1)


# there is one more solution using bit manipulation 
# using ( 8 4 2 1 ) select one or not 
 
