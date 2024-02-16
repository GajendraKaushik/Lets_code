# Brute force approach
def longest_subarray_with_zero_sum(nums):
    n = len(nums)
    max_len = 0 
    for i in range(n):
        sum_zero = 0 ; 
        for j in range(i, n):
            sum_zero = sum_zero + nums[j]
            if sum_zero == 0 :
                temp_len = j - i +1
                if temp_len > max_len:
                    max_len = temp_len
    print("max_len : ", max_len)

arr = [1, 3, -5, 6, -2]
longest_subarray_with_zero_sum(arr)

# optimal Solution with good approach

def optimal_approach_using_prefix_sum(nums):
    n = len(nums)
    max_len = 0
    sum_zero = 0
    hashmap = {}
    for i in range(n):
        sum_zero = sum_zero + nums[i]
        if sum_zero == 0 :
            max_len = i + 1
        else:
            if sum_zero in hashmap :
                temp_len = i - hashmap[sum_zero]
                max_len = max(max_len, temp_len)
            else:
                hashmap[sum_zero] = i 
    print("maxi :", max_len)
            

arr = [9, -3, 3, -1, 6, -5] #[1, 2, -2, 4, -4]
optimal_approach_using_prefix_sum(arr)

# Kadane's algorithm for maximum sub array sum 

def max_sum_arraySum_Kadanes_algo(nums):
    max_sum = nums[0] 
    sum = 0 
    for i in range(len(nums)):
        sum = sum + nums[i]
        max_sum = max(sum, max_sum)
        if sum < 0:
            sum =0
    print(max_sum)

arr = [5,4,-1,7,8]#[-2,1,-3,4,-1,2,1,-5,4]
max_sum_arraySum_Kadanes_algo(arr)
        



