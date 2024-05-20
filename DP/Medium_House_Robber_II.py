"""
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

 

Example 1:

Input: nums = [2,3,2]
Output: 3
Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2), because they are adjacent houses.
Example 2:

Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.
Example 3:

Input: nums = [1,2,3]
Output: 3

"""
def tabulation(n,nums, dp):
    dp[0] = nums[0]

    for i in range(1,n):
        pick = nums[i]
        if i > 1:
            pick += dp[i-2]
        notPick = 0 + dp[i-1]

        dp[i] = max(pick, notPick)
    return dp[n - 1]
def f(nums):
    n = len(nums)
    dp = [-1]*n
    temp = nums[:n-1]
    temp1= nums[1:]
    ans1 = tabulation(len(temp),temp, dp)
    ans2 = tabulation(len(temp1), temp1, dp)

    print(max(ans1, ans2))

nums = [2,3,2]

f(nums)

def spaceOptimizationApproch(n, nums):
    prev = nums[0]
    prev2 = 0

    for i in range(n):
        pick = nums[i]
        if i> 1:
            pick += prev2
        notPick = 0 + prev

        curr_i = max(pick, notPick)
        prev2 = prev
        prev = curr_i
    return prev

nums1 = [1,2,3,1] 
ans3 = spaceOptimizationApproch(len(nums1), nums1)
print(ans3)

    