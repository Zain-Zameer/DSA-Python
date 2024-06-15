def countingSort(array):
    max_value = max(array)
    counts=[0]*(max_value+1)
    
    # calculating occurences
    for num in array:
        counts[num]+=1

    sorted_arr=[]

    for i in range(len(counts)):
        sorted_arr.extend([i]*counts[i])
    
    return sorted_arr



if __name__=="__main__":
    array = [4,3,21,8,0,9]
    print(countingSort(array))