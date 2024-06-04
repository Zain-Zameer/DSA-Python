def quickSort(array,start,end):
    if start<end:
        part = partition(array,start,end)
        quickSort(array,start,part-1)
        quickSort(array,part+1,end)

def partition(array,start,end):
    pivot= end
    i = start-1
    for j in range(start, end):
        if(array[j]<array[pivot]):
            i+=1
            array[i], array[j] = array[j], array[i]
    array[i + 1], array[end] = array[end], array[i + 1]
    return i+1
            

array= [4,2,5,7,2,1,0,6,3]
quickSort(array,0,len(array)-1)
print(array)