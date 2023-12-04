# 4sum Optimal approach using two first sort the array then use pointer

def Optimal_4Sum(nums, target):
    n = len(nums)
    ans = []
    nums.sort()
    for i in range(n):
        if i !=0 and nums[i] == nums[i-1]:
            continue
        for j in range(i+1, n):
            print(nums[i])
            if j > i +1 and nums[j] == nums[j-1]:
                continue
            k = j+1
            l = n-1
            print(n, l, nums[l])

            while k<l:
                total_sum = nums[i] + nums[j]+ nums[k] + nums[l]
                print(total_sum,"sum")
                if total_sum < target:
                    k += 1
                elif total_sum > target:
                    l -= 1
                else:
                    temp = [nums[i], nums[j], nums[k], nums[l]]
                    ans.append(temp)
                    k += 1
                    l -= 1 
                    while k <l and nums[k] == nums[k-1]:
                        k += 1
                    while k < l and l-1 !=k and nums[l] == nums[l+1]:
                        l -= 1
    print(ans)
    return (ans)

nums = [-1,0,-5,-2,-2,-4,0,1,-2]#[2,2,2,2,2] 
ans = Optimal_4Sum(nums, -9)
for it in ans:
    print("[", end="")
    for i in it:
        print(i, end=" ")
    print("]", end="")
print()   


# kSum soluton

def fourSum( nums, target):
        nums.sort()
        
        solution = []
        rest = []

        def kSum(k, start, target):
            if target > 0 and nums[start] > target:
                return
            if target < 0 and nums[start] >= 0:
                return

            if k == 2:
                l, r = start, len(nums)-1
                while l < r:
                    if nums[l] + nums[r] < target:
                        l += 1
                    elif nums[l] + nums[r] > target:
                        r -= 1
                    else:
                        solution.append(rest + [nums[l], nums[r]])
                        l += 1
                        while l < r and nums[l] == nums[l - 1]:
                            l += 1
            else:
                for i in range(start, len(nums) - k + 1):
                    if i > start and nums[i] == nums[i - 1]:
                        continue
                    rest.append(nums[i])
                    kSum(k - 1, i + 1, target - nums[i])
                    rest.pop()
                return
        
        kSum(4, 0, target)
        return solution 
