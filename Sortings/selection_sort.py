arr= [64, 25, 12, 22, 11]
def selectionSort(arr):
    for j in range(len(arr)-1):
        min = j
        for i in range(j+1, len(arr)):
            if arr[min] > arr[i]:
                min = i
        [arr[j],arr[min]] = [arr[min], arr[j]]
    print(arr)

selectionSort(arr)


