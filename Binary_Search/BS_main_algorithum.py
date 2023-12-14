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
        if nums[mid] == target:
            return mid
        else:
            if nums[mid] > target:
                return Binary_Search(nums, start, mid - 1, target)
            else:
                return Binary_Search(nums, mid + 1, end, target)



arr = [4,5,6,7,0,1,2,3]#[5,6,10,12,15,18,20]
n = len(arr) - 1 
ans = Binary_Search(arr, 0, n, 0)
print(arr[ans])


