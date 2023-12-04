#https://takeuforward.org/data-structure/merge-two-sorted-arrays-without-extra-space/

def Brute_approach(nums1, nums2):
    n = len(nums1)
    m = len(nums2)
    print(n, m)
    ans =[0]*(n+m)
    i = 0
    j = 0
    k = 0
    while(n > i and m > j):
        print(j,i)
        if nums1[i] <= nums2[j]:
            ans[k] = nums1[i]
            i += 1
            k += 1
        else:
            ans[k] = nums2[j]
            j += 1 
            k += 1
    while(n>i):
        ans[k] = nums1[i]
        i += 1
        k +=1 
    while(m > j):
        ans[k] = nums2[j]
        j +=1
        k +=1
    print(ans)
    for i in range(n+m):
        if i < n:
            nums1[i] = ans[i]
        else:
            nums2[i-n] = ans[i]

arr1 = [1, 4, 8, 10]
arr2 = [2, 3, 9]
n = 4
m = 3
Brute_approach(arr1, arr2)
print("out Put of Brute approach  ")
print(arr1)
print(arr2)

# Optimal Approach 

def optimal_approach(nums1,nums2):
    n = len(nums1)
    m = len(nums2) 
    i = n-1
    j = 0 

    while i >=0  and  j < m:
        if  nums1[i] > nums2[j] :
            nums1[i] , nums2[j] = nums2[j], nums1[i]
            i -= 1
            j += 1
        else:
            break
    nums1.sort()
    nums2.sort()

arr11 = [1,3,5,7]
arr22 = [0,2,6,8,9]
n = 4
m = 3
optimal_approach(arr11, arr22)
print("out Put of optimal approach ")
print(arr11)
print(arr22)

#Optimal Solution 2 

def spwapleftright(nums1, nums2, ind1, ind2):
    if nums1[ind1] > nums2[ind2]:
        temp = nums1[ind1]
        nums1[ind1] = nums2[ind2]
        nums2[ind2] = temp 
        #nums1[ind1], nums2[ind2] = nums2[ind2], nums1[ind1]
def Optimal_approach_2(nums1, nums2, n, m):
    len = n + m 
    gap = (len // 2) + (len % 2)

    while gap > 0 :
        left  = 0 
        right = left + gap
        
        # first right will exit 
        while right < len :
            #case one left is in nums1  and write is in nums2
            if left < n and right >= n:
                spwapleftright(nums1, nums2, left , right - n)
             
            #case 2 both pointers are in array nums2   
            elif left >= n:
                spwapleftright(nums2, nums2, left - n , right - n)
            
            #case 3 both pointers are in nums1
            else:
                spwapleftright(nums1, nums1, left , right)
            left += 1
            right += 1 
        # break if iteration gap =1 is completed 
        if gap == 1:
            break
        gap = (gap // 2) + (gap % 2)



nums1 = [1,4,8,10]
nums2 = [2,3,9]
n = 4
m = 3 
Optimal_approach_2(nums1, nums2, n, m)
print("out Put of optimal approach_2 ")
print("nums1 : ", nums1)
print("nums2 :", nums2)
 

# https://leetcode.com/problems/merge-sorted-array/ 

def merge(nums1, num2, n ,m ):
    last = m + n - 1

    while m > 0 and n > 0 :

        if nums1[m-1] < nums2[n-1]:
            nums1[last] = nums2[n-1]
            n -= 1
        else:
            nums1[last] = nums1[m-1]
            m -= 1
        last -= 1
    while n > 0 :
        nums1[last] = nums2[n-1]
        n, last = n-1, last -1
    
    return nums1 








    