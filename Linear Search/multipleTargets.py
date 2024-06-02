def linearSearch(array,targets):
    targetsFound= []
    for target in targets:
        for i in range(0,len(array)):
            if array[i]==target and array[i-1]!=target:
                targetsFound.append(i)
    
    return targetsFound




array = [1,2,2,2,3,3,4,5,6,7,8,9,10,11,12,13]
targets = [2,5,7]
print(linearSearch(array,targets))