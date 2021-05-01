class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next

class LinkedList:
    def __init__(self):
        self.head= None
        
    def insert_begining(self, data):
        node=Node(data,self.head)
        self.head=node
        
    def print(self):
        if self.head is None:
            print("Linked list is empty")
            return
        itr = self.head
        llstr=''
        while itr:
            llstr += str(itr.data) + '--->'
            itr=itr.next

        print(llstr)  
        itr.next=Node(data, None)


if __name__=='__main__':
    ll=LinkedList()
    ll.insert_begining(5)
    ll.insert_begining(68)
    ll.print()
