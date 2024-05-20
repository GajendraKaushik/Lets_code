"""
Given a number of stairs and a frog, the frog wants to climb from the 0th stair to the (N-1)th stair. 
At a time the frog can climb either one or two steps. 
A height[N] array is also given. Whenever the frog jumps from a stair i to stair j, 
the energy consumed in the jump is abs(height[i]- height[j]), where abs() means the absolute difference.
We need to return the minimum energy that can be used by the frog to jump from stair 0 to stair N-1.

"""
import sys
def f(n, dp, arr):
        if dp[n] != -1:
            return dp[n]
        if n == 0:
            return 0
        jumpTwo = sys.maxsize
        jumpOne = f(n-1, dp, arr)+ abs(arr[n-1] - arr[n])
        if n > 1:
            jumpTwo = f(n-2, dp, arr)+ abs(arr[n-2] - arr[n])
        dp[n] = min(jumpOne, jumpTwo)
        return dp[n] 
arr = [10,20,30,10]
n  = 4 
def memoaization(n, arr):
    dp = [-1]*n
    ans = f(n-1, dp, arr)
    return ans

ans = memoaization(4, arr)
print(ans)