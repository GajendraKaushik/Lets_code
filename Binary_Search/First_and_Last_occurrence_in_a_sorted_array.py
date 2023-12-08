#first and last accurance of an element in sorted array

def find_first_and_last(nums, target, isfirst):
    n = len(nums)
    ans = float('-inf')
    left = 0 
    right = n-1 
    while left <= right:
        mid = (left + right ) //2 
        if nums[mid] > target:
              right = mid -1 
        elif nums[mid] < target :
             left = mid + 1
        else:
            ans = mid
            # searching for first occurence in first half 
            if isfirst :
                right = mid - 1
            else:
                # searching for the second occurence in last half
                left = mid + 1 
    return ans 

def Bs_first_and_last(nums, target):
    first = find_first_and_last(nums, target, True)
    last  = find_first_and_last(nums, target, False)
    print(first, last)

arr = [3, 4, 13, 13, 13, 20, 40]
Bs_first_and_last(arr, 13)