class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
# +++ Navi approach using Brute force  whith O (n^3) time +++

        # n = len(nums)
        # large_sum = 0
        # for i in range(n):
        #     for j in range(i,n):
        #         temp_sum = 0
        #         for k in range(i, j+1):
        #             temp_sum += nums[k]
        #         if temp_sum > large_sum:
        #             large_sum = temp_sum
        #         print(temp_sum,"t")
        #     print(large_sum,"l")
                
        # print(large_sum)
        # return large_sum

# Batter approach using Brute force with time O(n^2) time +++ 
        # n = len(nums)
        # large_sum = float('-inf') 
        # if n == 1 :
        #     return nums[0]
        # for i in range(n):
        #     temp_sum = 0
        #     for j in range(i, n):
        #         temp_sum += nums[j]
        #         if temp_sum > large_sum:
        #             large_sum = temp_sum         
        # print(large_sum)
        # return large_sum

#+++ Optimal approach with Kadane’s Algorithm +++
        n = len(nums)
        lsum = float('-inf') 
        tsum = 0
        for i in range(n):
            tsum += nums[i]
            if tsum > lsum:
                lsum = tsum 
            if tsum < 0:
                tsum = 0  # we are putting sum = 0 here becouse if we carry negative number utther then it will reduce or sum 
        return lsum      
             



     