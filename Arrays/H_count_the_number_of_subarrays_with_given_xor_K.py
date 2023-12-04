# question link https://www.interviewbit.com/problems/subarray-with-given-xor/

def brutre_subarray_with_given_xor_k(nums,k):
    n = len(nums)
    count = 0
    for i in range(n):
        for j in range(i,n):
            xor = 0
            for l in range(i, j+1):
                xor = xor ^ nums[l]
            if xor == k :
                count +=1
    print(count)
            
    
arr = [4, 2, 2, 6, 4]
brutre_subarray_with_given_xor_k(arr, 6) 

# batter approach with O(n^2) complexity 

def better_subarray_with_given_xor_k(nums,k):
    n = len(nums)
    count = 0
    for i in range(n):
        xor =0
        for j in range(i,n):
            xor = xor ^ nums[j]
            if xor == k :
                count +=1
    print(count)
            
    
arr = [4, 2, 2, 6, 4]
better_subarray_with_given_xor_k(arr, 6) 

# optimal approach 
