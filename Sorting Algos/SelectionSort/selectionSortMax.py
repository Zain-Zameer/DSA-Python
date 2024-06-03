def selectionSort(array):
    for i in range(0,len(array)):
        maximum = findMinimum(array,i)
        temp = array[i]
        array[i] = array[maximum]
        array[maximum] = temp 
    return array    


def findMinimum(array,start):
    maximum = -1
    for i in range(start,len(array)):
        if(array[i]>array[maximum]):
            maximum = i
        
    return maximum



array = [1,2,3,4]
print(selectionSort(array))