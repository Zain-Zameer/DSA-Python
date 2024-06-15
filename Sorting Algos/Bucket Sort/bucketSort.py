def insertionSort(bucket):
    for i in range(1,len(bucket)):
        key=bucket[i]
        j = i -1
        while j>=0 and bucket[j]>key:
            bucket[j+1] = bucket[j]
            j-=1
        bucket[j+1]=key 

def bucketSort(array):
    n=len(array)
    buckets=[] for _ in range(n)]

    for num in array:
        bucketInt = int(n*num)
        buckets[bucketInt].append(num)
    
    for bucket in buckets:
        insertionSort(bucket)
    
    index = 0
    for bucket in buckets:
        for num in bucket:
            array[index]=num
            index+=1
    
array = [0.87,0.56,0.65,0.1234,0.665,0.3434]
bucketSort(array)
print(array)