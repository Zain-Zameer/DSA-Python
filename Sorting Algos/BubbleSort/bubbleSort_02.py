# sorting in descending order

def bubbleSort(array):
    for i in range(0,len(array)):
        for j in range(0,len(array)-1):
            if array[j]<array[j+1]:
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp 
    return array

array = [0,1,2,3,4,5,6,7,0]
print(bubbleSort(array))