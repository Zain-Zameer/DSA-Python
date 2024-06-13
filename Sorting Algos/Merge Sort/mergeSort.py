def mergeSort(array):
    if len(array)<=1:
        return array 
    mid = len(array)//2
    left = array[:mid]
    right = array[mid:]

    mergeSort(left)
    mergeSort(right)

    return mergeTwoSortedLists(left,right,array)

def mergeTwoSortedLists(a,b,array):

    len_a = len(a)
    len_b = len(b)
    i = j = k=0
    while(i<len_a and j<len_b):
        if a[i] <=b[j]:
            array[k] = a[i]
            i+=1
        else:
            array[k]=b[j]
            j+=1 
        k+=1

    while i<len_a:
        array[k] = a[i]
        i+=1 
        k+=1
    while j<len_b:
        array[k] = b[j]
        j+=1
        k+=1


if __name__=="__main__":
    test_cases=[
        [10,0,2,4,5,6,0,1,2,12],
        [4,4,2,1],
        [0,0,1,12,0]
    ]
    for array in test_cases:
        mergeSort(array)
        print(array)