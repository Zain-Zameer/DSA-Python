def linearSearch(array,target):
    for i in range(0,len(array)):
        if(array[i]==target):
            return i
    return -1

array = [2,3,4,5,6,7,8]
target = 5

print(linearSearch(array,target))


