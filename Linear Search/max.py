def linearSearch(array):
    maximum = -1
    for i in range(0,len(array)):
        if(array[i]>=maximum):
            maximum = array[i]
    return maximum

array = [1,2,3,4,5,6,7,8,100,22,33]
print(linearSearch(array))
