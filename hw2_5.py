class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Deque:
    def __init__(self):
        self.frt=None
        self.decSize=0
    def isEmpty(self):
        if self.decSize==0:
            return True
        return False

    def addRear(self,data):
        x=Node(data)
        if self.frt==None:
            self.frt=x
            self.decSize=self.decSize+1
        else:
            pre=self.frt
            while pre.next!=None:
                pre=pre.next
            pre.next=x
            self.decSize=self.decSize+1

    def addFront(self,data):
        x=Node(data)
        if self.frt==None:
            self.frt=x
            self.decSize=self.decSize+1
        else:
            x.next=self.frt
            self.frt=x
            self.decSize=self.decSize+1

    def removeFront(self):
        if self.decSize==0:
            print("Deque is Empty")
        else:
            x=self.frt
            self.frt=self.frt.next
            self.decSize=self.decSize-1
            del x

    def removeRear(self):
        if self.decSize==0:
            print("Deque is Empty")
        else:
            pre=self.frt
            old=None
            while pre.next!=None:
                old=pre
                pre=pre.next
            old.next=pre.next
            self.decSize=self.decSize-1
            del pre
        
    def getfront(self):
        if self.decSize==0:
            print(" Empty deque")
        else:
            return self.frt.data
        
    def getrear(self):
        if self.decSize==0:
            print("Empty deque")
        else:
            pre=self.frt
            while pre.next!=None:
                pre=pre.next
            return pre.data

    def Size(self):
        return self.decSize

if __name__== '__main__':
    d = Deque()
    d.addFront('cat')
    d.addRear('dog')
    d.addRear(6)
    d.addFront(True)
    d.removeFront()
    d.removeRear()
    print("\nfront element is ",d.getfront())
    print("\nrear element is ",d.getrear())