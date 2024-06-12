def shellSort(array):
    size = len(array)
    gap = size//2
    while gap > 0:
        for i in range(gap,size):
            anchor = array[i]
            j=i
            while(j>=gap and array[j-gap] > anchor):
                array[j]=array[j-gap] 
                j-=gap
            array[j]=anchor    
        gap//=2        

if __name__=="__main__":
    array = [21,38,29,17,4,25,11,32,9]
    shellSort(array)
    print(array)