"""
Problem: 

Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.

Each number in candidates may only be used once in the combination.

Note: The solution set must not contain duplicate combinations.

 

Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8
Output: 
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]
Example 2:

Input: candidates = [2,5,2,1,2], target = 5
Output: 
[
[1,2,2],
[5]
]
"""
def Better_approach(candidates, target):
    ans = []
    candidates.sort()
    def Combination_Sum_II(index, target, subArray):
        if index == len(candidates):
            if target == 0:
                ans.append(subArray.copy())
                return
            return 
            
        if candidates[index] <= target:
            subArray.append(candidates[index])
            Combination_Sum_II(index +1, target - candidates[index], subArray)
            subArray.remove(candidates[index])
        Combination_Sum_II(index + 1, target, subArray)
    
    Combination_Sum_II(0, target, [])
    
    tuple_list = set(tuple(i) for i in ans)
    ans = [list(i) for i in tuple_list]
    return ans

# candidates =  [10,1,2,7,6,1,5]
# target = 8
# ans  = Better_approach(candidates, target)

# print(ans)

def Optimal_approach(candidates, target):
    """
    Param: 
    Target:
    Return:
    """
    ans = []
    candidates.sort()
    def Combination_Sum_II(index, target, subArray):
        if target == 0 :
            ans.append(subArray.copy())
            return
        
        for i in range(index, len(candidates)):
            if i > index and candidates[i] == candidates[i - 1]:
                continue
            if candidates[i] > target:
                break
            subArray.append(candidates[i])
            Combination_Sum_II(i + 1, target - candidates[i], subArray)
            subArray.remove(candidates[i])
    Combination_Sum_II(0, target, [])
    return ans

candidates =  [10,1,2,7,6,1,5]
target = 8
ans  = Optimal_approach(candidates, target)
print(ans)


    
        
        