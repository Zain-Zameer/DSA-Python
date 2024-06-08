class Node:
    def __init__(self,data=None,next=None):
        self.data = data 
        self.next = next 

class linkedList:
    def __init__(self):
        self.head = None 
        
    def insert_at_beginning(self,data):
        node = Node(data,self.head)
        self.head = node 

    def insert_at_end(self,data):
        if self.head is None:
            self.head = Node(data,None)
            return 
        itr = self.head 
        while itr.next:
            itr = itr.next 
        
        itr.next = Node(data,None)
    
    def print(self):
        if self.head is None:
            print("Linked list is empty")
            return 
        itr = self.head 
        listStr = ''
        while(itr):
            if(itr.next):
                listStr+= str(itr.data)+ '-->'
            else:
                listStr+= str(itr.data)
            itr = itr.next 
        print(listStr)
    
    def insert_values(self,data_list):
        self.head= None 
        for data in data_list:
            self.insert_at_end(data)

    def get_length(self):
        count = 0
        itr = self.head 
        while(itr):
            count+=1
            itr = itr.next 
        return count
    
    def remove_at(self,index):
        if index<0 or index >= self.get_length():
            raise Exception("Invalid index")
        if index==0:
            self.head = self.head.next
            return 
        count = 0
        itr = self.head
        while(itr):
            if count ==index-1:
                itr.next= itr.next.next
                break
            itr = itr.next
            count+=1
    
    def insert_at(self,index,data):
        if index<0 or index >= self.get_length():
            raise Exception("Invalid index")

        if index==0:
            self.insert_at_beginning(data)
            return 
        
        if index==self.get_length() -1:
            self.insert_at_end(data)
            return 

        count = 0
        itr = self.head
        while(itr):
            if(count==index-1):
                node = Node(data,itr.next)
                itr.next = node 
                break
            itr = itr.next
            count+=1

    #assignment

    # def insert_after_value(self, data_after, data_to_insert):
       

    # def remove_by_value(self, data):
        


if __name__ == '__main__':
    ll = linkedList()
    ll.insert_at_beginning(4)
    ll.insert_at_beginning(42)
    ll.insert_at_beginning(43)
    ll.insert_at_end(666)
    ll.insert_at_end(666)
    ll.insert_at_end(666)

    ll.insert_values([1,2,3,4,5,6,7,23,4,23,6,346,346,46,254])
    ll.remove_at(2)
    ll.insert_at(2,"Jacob")
    ll.print()
