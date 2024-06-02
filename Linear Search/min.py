def linearSearch(array):
    minimum = array[0]
    for i in range(0,len(array)):
        if(array[i]<=minimum):
            minimum = array[i]
    return minimum

array = [7,8,9,0,1,10,11,13,12]
print(linearSearch(array))
