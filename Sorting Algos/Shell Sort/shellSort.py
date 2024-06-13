def shellSort(array):
    size = len(array)
    gap = size // 2
    while gap > 0:
        for i in range(gap,size):
            anchor = array[i]
            j = i 
            while(j>=gap and array[j-gap] > anchor):
                array[j]=array[j-gap]
                j-=gap 
            array[j] = anchor 
        gap = gap // 2

if __name__=="__main__":
    test_cases= [
        [12,1,3,4,2,2,0,1],
        [0,1,2,0]
    ]
    for array in test_cases:
        shellSort(array)
        print(array)
    