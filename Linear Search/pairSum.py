def linearSearch(array,targetSum):
    check = [-1,-1]
    for i in range(0,len(array)):
        for j in range(0,len(array)):
            if array[i]+array[j] == targetSum:
                check[0] = i
                check[1] = j
    return check

array = [2,3,4,6]
targetSum = 7

print(linearSearch(array,targetSum))