#here creating the class for creating the node with data and next property

class node:
    def __init__(self,data):
        self.data=data
        self.next=None
    
class linked:
    def __init__(self):
        self.head=None
    # create a function to traverse the linked list..
    
    def traverse(self):
        t=self.head
        while(t!=None):
            print(t.data)
            t=t.next
            
#when i create obj for this class , it create a head = none
llist=linked() 
n=int(input(" enter how any element to add in linked list :"))
for i in range(n):
    if i==0:
        llist.head=node(int(input("enter the 1st num:")))
        temp=llist.head
    else:
        temp.next=node(int(input("enter the element:")))
        temp=temp.next
else:
     print("linked list created successfully ..")
     if int(input(" want to traverse :(1/0)"))==1:
         llist.traverse()
     else:
         print(" thank you ...")
     
    
