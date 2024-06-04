def message(n):
    if(n>0):
        print('Hello World')
        return message(n-1)
message(5)