def nums(value):
    if(value<=1):
        return value
    return str(value)+" "+str(nums(value-1))

print(nums(5))