# BS concept 

def Binary_Search(nums, start, end, target):
    if start == end:
        if nums[start] == target:
            return start
        else:
            return -1 
    else:
        n = start + end 
        mid = n//2 
        print(mid)
        if nums[mid] == target:
            return mid
        else:
            if nums[mid] > target:
                return Binary_Search(nums, start, mid - 1, target)
            else:
                return Binary_Search(nums, mid + 1, end, target)



arr = [5,6,10,12,15,18,20]
n = len(arr) - 1 
ans = Binary_Search(arr, 0, n, 18)
print(ans)
print(arr[ans])
