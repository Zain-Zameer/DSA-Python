def insertionSort(array):
    for i in range(1,len(array)):
        key = array[i]
        j = i-1
        while(j>=0 and key<array[j]):
            array[j+1] = array[j] 
            j= j -1
        array[j+1] = key
    return array




array = [4,3,5,2,1,0,5,7]
print(insertionSort(array))