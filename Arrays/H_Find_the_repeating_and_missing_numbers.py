# navie approach using linear search find the number of repeations of number in rnage of 1- N
def hashmap_approach(nums):
    n = len(nums)
    hashmap = {}
    ans =[]
    # sum of n natural number 
    sum = n*(n+1) // 2
    
    # map to find the duplicate 
    for i in range(n):
        if nums[i] in hashmap:
            hashmap[nums[i]] += 1
        else:
            hashmap[nums[i]] = 1

    key_list = list(hashmap.keys())
    val_list = list(hashmap.values())
    # calculating missing number 
    for i in range(len(key_list)):
        sum = sum - key_list[i]

    # getting the duplicate value 
    duplicate = key_list[val_list.index(2)]
    ans.append(duplicate)
    ans.append(sum)
    return ans

nums = [3,1,2,5,3]
ans = hashmap_approach(nums)
print(ans,"using func")

def hashArray_approach_2(nums):
    n = len(nums)

    hash =[0]*(n+1)

    for i in range(n):
        hash[nums[i]] +=1
    print(hash)

    duplicate , missing = -1, -1 

    for i in range(1, n+1):
        if hash[i] == 2:
            duplicate = i 
        elif hash[i] == 0:
            missing = i
        if duplicate !=-1 and missing != -1:
            break
    return [duplicate, missing]


nums = [3,1,2,5,3]
ans = hashArray_approach_2(nums)
print(ans,"using array")

# Optimal approach using math :

def optimal_approach(nums):
    # s-Sn = x -y ( x is repeatign number y is missing number) 
    # s2 - S2n = x^2 - Y^2 [(x-y) (x+y)]
    s, s2 = 0, 0
    n = len(nums)
    sn = n*(n+1)//2 
    s2n = (n*(n+1)*(2*n+1))  // 6 

    for i in range(n):
        s = s + nums[i]
        s2 = s2 +(nums[i]*nums[i])
    
    val1  = s-sn # s-sn = x-y 
    val2 = s2-s2n # s2-s2n = x+y 
    val2 = val2 // val1 # x+y = (X^2-Y^2)/(X-Y)
    # calculating the number of repeated and missing number 
    x = (val1+val2)  // 2 # 
    y = x - val1

    return [x, y]

nums = [3,1,2,5,3]
ans = optimal_approach(nums)
print(ans,"using optimal")
