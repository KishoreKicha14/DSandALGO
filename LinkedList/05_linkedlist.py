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
    def checkcircular(self):
        actucal=self.head
        f=0
        while(actucal.link!=None):
            actucal=actucal.link
            if(actucal.link==self.head):
                f=1
                break
        if(f==1):
            print("circular")
        else:
            print("not circular")
            
            
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
ll.checkcircular()
