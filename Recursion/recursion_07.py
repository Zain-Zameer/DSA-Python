def binarySearch(array,start,end,target):
    mid = (start+end)//2
    if(start<=end):
        if(array[mid]<target):
            return binarySearch(array,mid+1,end,target)
        elif(array[mid]>target):
            return binarySearch(array,start,mid-1,target)
    return mid
    
    

array = [1,2,3,4,5,6,7,8,9,10]
target = 9
print(binarySearch(array,0,len(array)-1,target))
    