"""
Find all valid combinations of k numbers that sum up to n such that the following conditions are true:

Only numbers 1 through 9 are used.
Each number is used at most once.
Return a list of all possible valid combinations. The list must not contain the same combination twice, and the combinations may be returned in any order.

Example 1:

Input: k = 3, n = 7
Output: [[1,2,4]]
Explanation:
1 + 2 + 4 = 7
There are no other valid combinations.
Example 2:

Input: k = 3, n = 9
Output: [[1,2,6],[1,3,5],[2,3,4]]
Explanation:
1 + 2 + 6 = 9
1 + 3 + 5 = 9
2 + 3 + 4 = 9
There are no other valid combinations.
Example 3:

Input: k = 4, n = 1
Output: []
Explanation: There are no valid combinations.
Using 4 different numbers in the range [1,9], the smallest sum we can get is 1+2+3+4 = 10 and since 10 > 1, there are no valid combination.
"""


def combinationSum3(self, k: int, n: int):
    ans = []
    nums = [1,2,3,4,5,6,7,8,9]
    def reccursiveSum3(index, k, subArray, sum1):
        # Base case 
        if k == 0 and sum1 == n:
            print(subArray)
            ans.append(subArray.copy())
            return
        if index == len(nums):
            print(index)
            return 
        subArray.append(nums[index])
        reccursiveSum3(index + 1, k-1, subArray, sum1 + nums[index])
        subArray.remove(nums[index])
        reccursiveSum3(index + 1, k, subArray, sum1)
    reccursiveSum3(0,k,[],0)
    return ans