def linearSearch(array,target):
    check = [-1,-1]
    for i in range(0,len(array)-1):
        if(array[i]==target and array[i-1]!=target):
            check[0] = i
        if(array[i] == target and array[i+1]!=target):
            check[1] = i
    return check

array = [4,4,4,56,8]
target = 4

print(linearSearch(array,target))