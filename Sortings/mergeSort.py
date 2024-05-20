import math
arr = [5,4,3,2,1]
def merge(arr, low, mid, high):
    left = low
    right = mid+1
    temp = []
    cnt = 0
    while left <= mid and right <= high:
        if arr[left]>arr[right]:
            temp.append(arr[right])
            cnt += (mid - left + 1)
            right += 1
            
        else:
            temp.append(arr[left])
            left += 1

    while left <= mid:
            temp.append(arr[left])
            left += 1
    
    while right <= high:
            temp.append(arr[right])
            right += 1
    
    for i in range(low, high+1):
         arr[i] = temp[i-low]
    return cnt

# def merge(arr, low, mid, high):
#     left = low
#     right = mid + 1
#     temp = []
#     cnt = 0
#     while left <= mid and right <= high:
#         if (arr[left] <= arr[right] ):
#             temp.append(arr[left])
#             left +=1
#         else:
#             temp.append(arr[right])
#             cnt += (mid - left + 1 )
#             right += 1 


#         # if arr[left]>= arr[right]:
#         #     temp.append(arr[right])
#         #     cnt += (mid - left + 1)
#         #     print(cnt)
#         #     print(left, "left")
#         #     right += 1
#         # else:
#         #     temp.append(arr[left])
#         #     left += 1

#     while left <= mid:
#         temp.append(arr[left])
#         left += 1

#     while right <= high:
#         temp.append(arr[right])
#         right += 1

#     for i in range(low, high + 1):
#         arr[i] = temp[i - low]
#     return cnt


def mergeSort(arr, low, high):
    cnt = 0
    if low >= high:
         return cnt
    mid = math.floor((low+high)//2)
    cnt += mergeSort(arr, low, mid)
    cnt += mergeSort(arr, mid+1, high)
    print(cnt)
    cnt += merge(arr, low, mid, high)
    return cnt

print(arr)
ans = mergeSort(arr, 0, len(arr)-1)
print(ans)
print(arr)