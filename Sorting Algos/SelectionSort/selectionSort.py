def selectionSort(array):
    for i in range(0,len(array)):
        minimum = findMinimum(array,i)
        temp = array[i]
        array[i] = array[minimum]
        array[minimum] = temp 
    return array    


def findMinimum(array,start):
    minimum = start
    for i in range(start,len(array)):
        if(array[i]<array[minimum]):
            minimum = i
        
    return minimum



array = [5,6,3,2,7,8,1,4]
print(selectionSort(array))