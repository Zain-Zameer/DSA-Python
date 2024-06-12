class Node:
    def __init__(self,data,next=None,prev=None):
        self.data = data 
        self.next = next 
        self.prev = prev 

class circularDoubLL:
    def __init__(self):
        self.head = None 
    def insert_at_beginning(self,data):
        node = Node(data)
        if self.head is None:
            node.next = node 
            self.head = node 
        else:
            itr = self.head
            while itr.next !=self.head:
                itr = itr.next 
            node.next=self.head
            itr.next=node 
            self.head = node 
    def insert_at_end(self,data):
        node = Node(data)
        if self.head is None:
            node.next = node 
            self.head = node 
        else:
            itr = self.head 
            while(itr.next !=self.head):
                itr = itr.next 
            node.next = self.head 
            itr.next = node 
            
    def print(self):
        if self.head is None:
            print("Doubly circular linked list is empty")
            return 
        else:
            itr = self.head 
            listStr = ''
            while(itr):
                listStr+=str(itr.data)+'-->'
                itr = itr.next 
                if itr==self.head:
                    break 
            print(listStr)

if __name__=="__main__":
    cdll = circularDoubLL()
    cdll.insert_at_beginning(2)
    cdll.insert_at_beginning(23)
    cdll.insert_at_beginning(23)
    cdll.insert_at_end(222)
    cdll.print()
