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
        r=[]
        while actucal!=None:
            r.append(actucal.data)
            actucal=actucal.link
        print("->".join(r))
    def swap(self):
        actucal=self.head
        if(self.size%2==0):
            while(actucal!=None):
                temp=actucal.data
                actucal.data=actucal.link.data
                actucal.link.data=temp
                actucal=actucal.link.link
        else:
            while(actucal.link!=None):
                temp=actucal.data
                actucal.data=actucal.link.data
                actucal.link.data=temp
                actucal=actucal.link.link
            
        
            
            
node1=Node("A")       
node2=Node("B")
node3=Node("C")
node4=Node("D")
node5=Node("E")
node6=Node("F") 

ll1=LinkedList()
ll1.insertend(node1)
ll1.insertend(node2)
ll1.insertend(node3)
ll1.insertend(node4)
ll1.insertend(node5)
#ll1.insertend(node6)
ll1.transveral()
ll1.swap()
ll1.transveral()
