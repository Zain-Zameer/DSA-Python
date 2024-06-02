def linearSearch(array,target):
    for i in range(0,len(array)):
        for j in range(0,len(array[i])):
            if(array[i][j]==target):
                return i,j
    return -1

array = [
    [1,2,3,4],
    [5,6,7,8]
]
target = 5

print(linearSearch(array,target))