arr = [12, 11, 13, 5, 6]

def insertionSort(arr):
    n = len(arr)
    for i in range(1,n):
        for j in range(i-1, -1, -1):
            if arr[j] > arr[j+1]:
                [arr[j], arr[j+1]] = [arr[j+1], arr[j]]
    print(arr)

insertionSort(arr)
