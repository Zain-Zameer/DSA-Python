# sorting in list according to the length of string in ascending order
def bubbleSort(array):
    for i in range(0,len(array)):
        for j in range(0,len(array)-1):
            if len(array[j])>len(array[j+1]):
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp 
    return array

array = ["Hello","Hell","Hel","He","H"]
print(bubbleSort(array))