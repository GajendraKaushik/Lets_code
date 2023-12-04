# Bruteforce technique 
# def brute_approach(nums):
#     n = len(nums)
#     cnt = 0 
#     for i in range(n):
#         for j in range(i+1, n):
#             if nums[i] > 2*nums[j]:
#                 cnt +=1
#     print(cnt)
# nums1 = [5,4,3,2,1]
# count = brute_approach(nums1)
# print(count, "cnt")


# implementing the solution using merge sort 
import math
def merge(nums, low, mid, high):
    temp = []
    left = low 
    right = mid+1 
    cnt = 0

    while(left <= mid and right <= high):

        if (nums[left] <= nums[right] ):
            temp.append(nums[left])
            left +=1 
        else:
            temp.append(nums[right])
            cnt += (mid - left +1 )
            right += 1 

    while (left <= mid):
        temp.append(nums[left])
        left += 1
    while(right <= high):
        temp.append(nums[right])
        right += 1
    for i in range(low, high + 1):
        nums[i] = temp[i - low]
    print(nums)
    
def countREversPair(nums, low, mid, high):
    right = mid +1
    cnt = 0  
    for i in range(low, mid + 1):
        while right <= high and nums[i] > 2* nums[right]:
            right += 1
        cnt += (right - (mid + 1))
    return cnt

def merge_sort(nums, low ,high):
    cnt = 0 
    if low >= high:
        return cnt
    mid = (low+high) // 2
    cnt += merge_sort(nums, low, mid)
    cnt += merge_sort(nums, mid + 1, high)
    cnt += countREversPair(nums, low, mid, high)
    merge(nums, low, mid, high)
    return cnt 

def Optimal_approach(nums):
    n = len(nums)
    return merge_sort(nums, 0, n-1)

nums = [2,4,3,5,1]
n = 5 
cnt = Optimal_approach(nums)
print(cnt,"merge")

