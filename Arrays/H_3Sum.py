# First approache is brute force use 3 for loops and find the  triplets 

# Second approach is use two for loop and a hashset to find the 3rd values.
def find_3Sum(nums, target):
    n = len(nums)
    setdata = set()
    for i in range(n):
        hashset = set()
        for j in range(i+1, n):
            k = target - (nums[i] + nums[j])
            if k in hashset:
                temp = [nums[i],nums[j], k]
                temp.sort()
                setdata.add(tuple(temp))
            hashset.add(nums[j])
    ans = list(setdata)
    return ans 

nums = [0,0,0] 
ans = find_3Sum(nums, 0)
for it in ans:
    print("[", end="")
    for i in it:
        print(i, end=" ")
    print("]", end="")
print()

# #rd aprroach is sort the array then use two pointer to solve it.
# time complexity O(n)
def Optimal_3sum_two_Pointer(nums):
    ans = []
    n = len(nums)
    nums.sort() # O(nlogn)
    for i in range(n):  # O(n)
        # we only wnat to unique elements 
        if i!=0 and  nums[i] == nums[i-1]:
            continue
        # initialized two pointer
        j = i+1
        k = n-1
        #finding the triplet
        while j<k : # O(n) approx
            total_sum = nums[i] + nums[j] + nums[k]
            if total_sum < 0:
                j += 1
            elif total_sum > 0:
                k -= 1
            else:
                temp = [nums[i], nums[j], nums[k]]
                ans.append(temp)
                j += 1
                k -=1
                # skiping the duplicagte elements
                while j < k and nums[j] == nums[j-1]:
                    j += 1
                while j < k and nums[k] == nums[k+1]:
                    k -= 1
    return ans

nums = [0,0,0] 
ans = find_3Sum(nums, 0)
for it in ans:
    print("[", end="")
    for i in it:
        print(i, end=" ")
    print("]", end="")
print()       

    