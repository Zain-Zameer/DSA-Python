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
    i=j=k=0
    while(i<len_a and j<len_b):
        if a[i]<= b[j]:
            array[k]=a[i]
            i+=1 
        else:
            array[k]=b[j]
            j+=1
        k+=1
            
    while i<len_a:
        array[k]=a[i]
        i+=1
        k+=1
    while j<len_b:
        array[k]=b[j]
        j+=1
        k+=1


if __name__=="__main__":
    test_cases=[
        [10,0,2,3,4,5,6,1,1],
        [4,4,2],
        [0,0,10,2]
    ]
    for test in test_cases:
        mergeSort(test)
        print(test)
