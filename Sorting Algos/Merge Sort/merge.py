def mergeSort(array):
    if len(array) <= 1:
        return array 
    
    mid = len(array) // 2 
    left = array[:mid]     
    right = array[mid:]
    
    left_sorted = mergeSort(left)  
    right_sorted = mergeSort(right) 
    
    return mergeTwoSortedLists(left_sorted, right_sorted)  

def mergeTwoSortedLists(a,b):
    sorted_list = []
    len_a = len(a)
    len_b = len(b)
    i=j=0
    while(i<len_a and j<len_b):
        if a[i]<= b[j]:
            sorted_list.append(a[i])
            i+=1 
        else:
            sorted_list.append(b[j])
            j+=1
            
    while i<len_a:
        sorted_list.append(a[i])
        i+=1

    while j<len_b:
        sorted_list.append(b[j])
        j+=1
    return sorted_list

if __name__ == "__main__":
    array = [7, 6, 5, 4, 3, 2, 1, 0, 44, 55, 77, 88]
    
    print(mergeSort(array)) 
