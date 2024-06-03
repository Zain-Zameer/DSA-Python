# sorting in ascending order

def bubbleSort(array):
    for i in range(0,len(array)):
        for j in range(0,len(array)-1):
            if array[j]>array[j+1]:
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp 
    return array

array = [5,4,3,2,1,5,0]
print(bubbleSort(array))