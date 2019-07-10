class Node(object):
    def __init__(self,data):
        self.data=data
        self.link=None
class LinkedList(object):
    def __init__(self):
        self.head=None
        self.size=0
            
    def insertend(self,data):
        if not self.head:
            self.head=data
        else:
            actucal=self.head
            while actucal.link!=None:
                actucal=actucal.link
            actucal.link=data
        self.size+=1
    def transveral(self):
        actucal=self.head
        while actucal!=None:
            print(actucal.data)
            actucal=actucal.link
    def checkcycle(self):
        slow=self.head
        fast=self.head
        f=0
        while(fast!=None)and(fast.link!=None):
            fast=fast.link.link
            slow=slow.link
            if(fast==slow):
                f=1
                break
        if(f==1):
            print("found cycle")
        else:
            print("no cycle")
            
            
node1=Node(10)       
node2=Node(20)
node3=Node(30)
node4=Node(40)
node5=Node(50)  

ll=LinkedList()
ll.insertend(node1)
ll.insertend(node2)
ll.insertend(node3)
ll.insertend(node4)
ll.insertend(node5)
ll.insertend(node1)
#ll.transveral()
ll.checkcycle()

ll1=LinkedList()
ll1.insertend(node1)
ll1.insertend(node2)
ll1.insertend(node3)
ll1.insertend(node4)
ll1.insertend(node5)
ll1.transveral()
ll1.checkcycle()
