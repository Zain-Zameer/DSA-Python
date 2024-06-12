class Node:
    def __init__(self,data,next=None):
        self.data = data 
        self.next = next 

class circularSinglyLL:
    def __init__(self):
        self.head = None 
    def insert_at_beginning(self,data):
        node= Node(data)
        if self.head is None:
            node.next = node 
            self.head=  node
        else:
            itr = self.head 
            while(itr.next !=self.head):
                itr = itr.next 
            node.next= self.head 
            itr.next= node 
            self.head = node 
    
    def insert_at_end(self,data):
        node = Node(data)
        if self.head is None:
            node.next = node
            self.head = node 
        else:
            itr = self.head 
            while(itr):
                itr=itr.next 
                if itr.next==self.head:
                    break 
            itr.next=node 
            node.next = self.head 
    
    def print(self):
        if self.head is None:
            print("circular singly linked list empty")
            return 
        itr = self.head 
        listStr = ''
        while(itr):
            listStr+=str(itr.data)+'-->'
            itr = itr.next
            if itr==self.head:
                break 
        print(listStr)

if __name__=="__main__":
    csll = circularSinglyLL()
    csll.insert_at_beginning(22)
    csll.insert_at_beginning(23)
    csll.insert_at_beginning(24)
    csll.insert_at_beginning(25)
    csll.insert_at_end(799)
    csll.print()