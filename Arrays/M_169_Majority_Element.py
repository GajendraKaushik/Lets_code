class Solution:
    def majorityElement(self, nums: List[int]) -> int:

#+++  Navie approach first approach but got time limit eceeded +++#
        # max_count = 0
        # index = 0
        # for i in range(len(nums)):
        #     temp = 1
        #     for j in range(i, len(nums)):
        #         if nums[i] == nums[j]:
        #             temp += 1
        #     if max_count < temp :
        #         max_count = temp 
        #         index = i
        #     if max_count > len(nums)//2:
        #         return nums[index]

#+++  Navie approach first approach but got time limit eceeded +++#

        # Hashmap = {}
        # n = len(nums)
        # for i in range(n):
        #     if nums[i] in Hashmap:
        #         Hashmap[nums[i]] += 1
        #     else:
        #         Hashmap[nums[i]] = 1 
        # for j in range(n):
        #     if Hashmap[nums[j]] > n//2:
        #         return nums[j]

#+++ Optimal approach with Moore’s Voting Algorithm o(n) time +++ 
        n = len(nums)
        cnt = 0 
        element = None

        for i in range (n):
            if cnt == 0:
                cnt = 1
                element = nums[i]
            elif nums[i] == element:
                cnt += 1 
            else:
                cnt -= 1
        cnt = 0
        for i in range(n):
            if nums[i] == element:
                cnt += 1

        if cnt > (n/2) :
            return element
        else:
            return -1 


