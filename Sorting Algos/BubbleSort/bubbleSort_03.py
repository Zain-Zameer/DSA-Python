# sorting in list according to the first letter ascending order
def bubbleSort(array):
    for i in range(0,len(array)):
        for j in range(0,len(array)-1):
            if array[j][0]>array[j+1][0]:
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp 
    return array

array = ["Aspirin","Ibuprofen","Paracetamol","Amoxcillin","Metaformin","Lisinopril"]
print(bubbleSort(array))