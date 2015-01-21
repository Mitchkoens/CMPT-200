####QuickSort####
def quickSort(arr):
    less = []
    pivotList = []
    more = []
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        for i in arr:
            if i < pivot:
                less.append(i)
            elif i > pivot:
                more.append(i)
            else:
                pivotList.append(i)
        less = quickSort(less)
        more = quickSort(more)
        print (less + pivotList + more)
        return less + pivotList + more
####MergeSort####
def mergeSort(arr):
    result = []
    if len(arr) < 20:
        return sorted(arr)
    mid = int(len(arr)/2)
    y = msort4(arr[:mid])
    z = msort4(arr[mid:])
    i = 0
    j = 0
    while i < len(y) and j < len(z):
            if y[i] > z[j]:
                result.append(z[j])
                j += 1
            else:
                result.append(y[i])
                i += 1
    result += y[i:]
    result += z[j:]
    return result
####CocktailSort####
def cocktailSort(arr):
    up = range(len(arr)-1)
    while True:
        for indices in (up, reversed(up)):
            swapped = False
            for i in indices:
                if arr[i] > arr[i+1]:  
                    arr[i], arr[i+1] =  arr[i+1], arr[i]
                    swapped = True
            if not swapped:
                return
            print(arr)
####InsertionSort
def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        low, up = 0, i
        while up > low:
            middle = (low + up) // 2
            if arr[middle] < key:
                low = middle + 1              
            else:
                up = middle
        arr[:] = arr[:low] + [key] + arr[low:i] + arr[i + 1:]
        print(arr)
####SelectionSort####
def selectionSort(arr):
    for i in range(0,len(arr)-1):
        mn = min(range(i,len(arr)), key=arr.__getitem__)
        arr[i],arr[mn] = arr[mn],arr[i]
    return arr
