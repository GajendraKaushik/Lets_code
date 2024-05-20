"""
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

Example 1:


Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
Example 2:

Input: height = [1,1]
Output: 1
"""
# here the question is to find the max area and approch we have to use is two pointer and traverse the array from both the sides of the array.

def Container_with_most_Water(arr):
    n = len(arr)
    i = 0
    j = n-1
    maxArea = 0
    while i<j:
        Len = j - i 
        currHeight = 0
        if arr[i]<arr[j]:
            currHeight = arr[i]
            i +=1
        else:
            currHeight = arr[j]
            j -= 1
        maxArea = max(maxArea, Len * currHeight)
    return maxArea

height = [1,8,6,2,5,4,8,3,7]
ans = Container_with_most_Water(height)
print(ans)
    
