#Problem : https://leetcode.com/problems/find-a-peak-element-ii/
# approach : find the peak element in all ond element and returen the greater from all element.

# this method will give us the peak element but we have to return the index of peak element 
def peak_in_oneD(nums):
    n = len(nums)
    if n == 0 or  nums[0] > nums[1]:
        return [0,nums[0]]
    elif nums[n-1] > nums[n-2]:
        return [n-1, nums[n-1]]

    left = 1
    right = n-2 
    while left <= right:
        mid = (left + right)//2 

        if nums[mid] > nums[mid-1] and nums[mid] > nums[mid + 1]:
            return [mid, nums[mid]]
        elif nums[mid] < nums[mid + 1]:
            left = mid + 1 
        else:
            right = mid - 1

# arr = [21,30,14]
# ans = peak_in_oneD(arr)
# print(ans)

def peak_in_2DArray(matrix):
    n = len(matrix)
    m = len(matrix[0])
    peak = 0
    ansarr = [0]*2
    for i in range(n):
        temp = peak_in_oneD(matrix[i])
        print(temp)
        if peak < temp[1] :
            peak = temp[1]
            ansarr[0] = i
            ansarr[1] = temp[0]
    print(ansarr)

mat = [[10,50,40,30,20],[1,500,2,3,4]]#[[1,4],[3,2]]#[[10,20,15],[21,30,14],[7,16,32]] 
ans2 = peak_in_2DArray(mat)

