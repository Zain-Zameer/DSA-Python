class Node:
    def __init__(self,data,next=None,prev=None):
        self.data=data 
        self.next = next 
        self.prev = prev 
class doublyLL:
    def __init__(self):
        self.head = None 
    def insert_at_beginning(self,data):
        node = Node(data,self.head)
        if self.head:
            self.head.prev = node 
        self.head = node 
    def insert_at_end(self,data):
        if self.head is None:
            self.head = Node(data)
            return 
        itr = self.head
        while(itr.next):
            itr = itr.next 
        node = Node(data,None,itr)
        itr.next = node
    def insert_values(self,dataList):
        self.head=None 
        for data in dataList:
            self.insert_at_end(data)
    def getLength(self):
        count = 0
        itr=self.head 
        while(itr):
            itr=itr.next 
            count+=1
        return count 
    def insert_at(self,index,data):
        if index==0:
            self.insert_at_beginning(data)
            return 
        if index==self.getLength()-1:
            self.insert_at_end(data)
            return 
        count = 0
        itr = self.head 
        while(itr):
            if(count==index-1):
                node = Node(data,itr.next,itr)
                if itr.next:
                    itr.next.prev=node
                itr.next=node
                break 
            itr = itr.next                
            count+=1

    def remove_at(self,index):
        if index<0 or index>=self.getLength():
            raise Exception("Invalid Index")
        if index==0:
            self.head = self.head.next
            if self.head:
                self.head.prev=None 
            return
        count = 0 
        itr = self.head 
        while(itr):
            if count==index-1:
                itr.next = itr.next.next
                if itr.next:
                    itr.next.prev = itr
                break 
            itr = itr.next 
            count+=1
    def insert_after_value(self,data_after,data_to_insert):
        if self.head is None:
            return 
        itr = self.head 
        while(itr):
            if itr.data==data_after:
                node = Node(data_to_insert,itr.next,itr)
                if itr.next:
                    itr.next.prev=node 
                itr.next=node 
                break 
            itr = itr.next
    
    def remove_by_value(self,data):
        if self.head is None:
            return 
        itr=self.head 
        while itr:
            if itr.data==data:
                if itr.prev:
                    itr.prev.next = itr.next 
                else:
                    self.head=itr.next 
                if itr.next:
                    itr.next.prev=itr.prev 
                break 
            itr=itr.next

    def print(self):
        if self.head is None:
            print("Doubly Linked List is empty")
            return 
        itr = self.head 
        ListStr = ''
        while(itr):
            if(itr.next):
                ListStr+=str(itr.data)+'-->'
            else:
                ListStr+=str(itr.data)

            itr = itr.next 
        print(ListStr)

if __name__=="__main__":
    dll = doublyLL()
    dll.insert_at_beginning(22)
    dll.insert_at_beginning(23)
    dll.insert_at_beginning(24)
    dll.insert_at_beginning(2255)
    dll.insert_at_beginning(22332)
    dll.insert_at_end(666)
    # dll.insert_values([2,3,4,5,6,7,8,9])
    dll.insert_at(1,24)
    # dll.remove_at(3)
    # dll.insert_after_value(24,55)
    # dll.remove_by_value(5)
    print(dll.getLength())
    dll.print()