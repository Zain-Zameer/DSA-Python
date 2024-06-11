def quickSort(array,start,end):
    if start<end:
        p = partition(array,start,end)
        quickSort(array,start,p-1)
        quickSort(array,p+1,end)

def partition(array,start,end):
    pivot = array[end]
    i = start -1
    for j in range(start,end):
        if array[j]<=pivot:
            i = i + 1
            array[i],array[j] = array[j],array[i]
    array[i+1],array[end] = array[end],array[i+1]
    return i + 1



array = [3,4,2,1,5,7,0,2]
quickSort(array,0,len(array)-1)
print(array)
