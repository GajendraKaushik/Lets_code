#problem:  https://leetcode.com/problems/merge-intervals/

def brute_approach(nums):
    n = len(nums)
    nums.sort()
    ans = []
    for i in range(n):
        start = nums[i][0]
        end = nums[i][1]
        if (len(ans)!=0 and end <= ans[len(ans)-1][1]):
            continue
        for j in range(i+1, n):
            if nums[j][0] <= end:
                end = max(end, nums[j][1])
            else:
                break
        ans.append([start, end])
    print(ans)
    return ans;

arr = [[1,3],[2,6],[8,10],[15,18]]
print(brute_approach(arr))

   
def better_approach(nums):
    n = len(nums)
    ans = []
    for i in range(n):
        start = nums[i][0]
        end = nums[i][1]
        if len(ans) == 0 or start > ans[len(ans)-1][1]:
            ans.append(nums[i])
        else:
            ans[len(ans)-1][1] = max(end, ans[len(ans)-1][1])
    return ans

arr = [[1,3],[2,6],[8,10],[15,18]]
print(better_approach(arr))
