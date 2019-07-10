class Node(object):
    def __init__(self,data):
        self.data=data
        self.link=None
class LinkedList(object):
    def __init__(self):
        self.head=None
        self.size=0
        
    def insertStart(self,data):
        newNode=Node(data)
        if (not self.head):
            self.head=newNode
        else:
            newNode.link=self.head
            self.head=newNode
        self.size+=1
            
    def insertend(self,data):
        newNode=Node(data)
        if not self.head:
            self.head=newNode
        else:
            actucal=self.head
            while actucal.link!=None:
                actucal=actucal.link
            actucal.link=newNode
        self.size+=1
    '''
    def insertat(self,data,k):
        c=0
        newNode=Node(data)
        if(k==0):
            newNode.link=self.head
            self.head=newNode
        else:
            c=
            actucal=self.head
            while actucal.link!=None and k>c:
                actucal=actucal.link
                c=c+1
            temp=actucal.link
            actucal.link=newNode
            newNode.link=temp
        self.size+=1
    '''
    def remove(self,data):
        actucal=self.head
        if actucal.data==data:
            self.head=actucal.link
            actucal.link=None
            print(actucal.data,"deleted")
        else:
            while actucal.link.data !=data:
                actucal=actucal.link
            temp=actucal.link
            actucal.link=actucal.link.link
            temp.link=None
            print(temp.data,"deleted")
        
    '''  
    def transveral(self):
        actucal=self.head
        while actucal!=None:
            print(actucal.data)
            actucal=actucal.link
    '''
    def find(self,k):
        actucal=self.head
        if k==1:
            return(actucal.data)
        elif(k>self.size):
            return("exceeds the limit")
        else:
            c=2
            while(k>=c):
                actucal=actucal.link
                c=c+1
            return(actucal.data)
       
            
        

ll=LinkedList()
ll.insertend("A")
ll.insertend("B")
ll.insertend("C")
ll.insertend("C")
ll.insertend("B")
ll.insertend("A")
d=ll.size
f=0
for i in range(1,d//2+1):
    if(ll.find(i)!=ll.find(d-i+1)):
        f=1
if(f==1):
    print("not palidrome")
else:
    print("palidrome")
