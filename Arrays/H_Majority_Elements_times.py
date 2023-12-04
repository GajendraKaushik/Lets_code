# Code for Majority Elements

# you can use brute force approach also 

def find_All_Majority_Elements(array):
    N = len(array)
    major = N//3
    major_elements = []
    dict_to_map_arrayElements = {}
    for i in range(N):
        if array[i] in dict_to_map_arrayElements:
            dict_to_map_arrayElements[array[i]] = dict_to_map_arrayElements[array[i]] + 1 
        else:
            dict_to_map_arrayElements[array[i]] = 1

    list_key = dict_to_map_arrayElements.keys()

    for i in list_key:
        if dict_to_map_arrayElements[i] > major:
            major_elements.append(i)
    print(major_elements, "map")

    # for i in range(len(array)):
    #     if dict_to_map_arrayElements[array[i]] > major:
    #         major_elements.append(array[i])
    
    # print(major_elements) # need to return as set ( oly unic values)

arr = [2, 2, 1, 1, 1, 2, 2]
find_All_Majority_Elements(arr)

# moors voting algorithums

def Moorse_voting_algo(arr):
    major_elements =[]
    n = len(arr)
    cnt1 =0; cnt2 = 0
    element1 = float('-inf'); element2 =float('-inf')

    for i in range(n):
        if cnt1 == 0 and element2 != arr[i]:
            cnt1 = 1
            element1 = arr[i]
        elif cnt2 == 0 and element2 !=  arr[i]: 
            cnt2 = 1
            element2 = arr[i]
        elif element1 == arr[i] :
            cnt1 +=1
        elif element2 == arr[i]:
            cnt2 += 1
        else:
            cnt1 -= 1; cnt2 -=1 
  
    cnt1 =0; cnt2 =0
    for i in  range (n):
        if element1 == arr[i] :
            cnt1 +=1
        if element2 == arr[i] :
            cnt2 +=1
    print(cnt1,cnt2)    
    if cnt1 > n//3:
        major_elements.append(element1)
    if cnt2 > n//3:
        major_elements.append(element2)
    
    print(major_elements, "Moor")

arr = [0,0,0]

Moorse_voting_algo(arr)


 # Solution from leet code

arr = [0,0,0] 
def majorityElement(nums):
        counts = {}
        for num in nums:
            counts[num] = counts.get(num, 0) + 1
        print(counts)

        res = []
        for num, count in counts.items():
            if count > len(nums)//3:
                res.append(num)

        print(res,"leetcode")
arr = [0,0,0]
majorityElement(arr)

       


## we get keyError when we try to access the key in ditc which is not present.