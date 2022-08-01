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
            
    # insertion in linkedlist at fornt of the linked list..
    
    def insertion_at_front(self):
        t=self.head
        self.head=node(int(input("enter a element to add at front ..")))
        self.head.next=t
        print(" insertion_at_front successfully..")
        if int(input("want to traverse (1/0)"))==1:
            self.traverse()
        else:
            print(" thank you ..")
    
    #insertion_at_end 
    
    def insertion_at_end(self):
        t=self.head
        while t.next!=None:
            t=t.next
        t.next=node(int(input("enter a element to add at end :")))
        self.traverse()
    
    
    
    
    
    
    
def main():
    print("1 . creation \n2. traverse \n 3.1 insertion_at_front \n 3.2 insertion_at_end \n enter your choise :")

#when i create obj for this class , it create a head = none

llist=linked() 
#linkedlist creation code wrap in the function..
def creation_linkedlist():
    n=int(input("linkedlist is created \n enter how any element to add in linked list :"))
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

creation_linkedlist()     
#llist.insertion_at_front()
llist.insertion_at_end()





