    
def main():
    print("0. Exit \n1. Creation \n2. Traverse \n3. Insertion\n4. Deletion \n5.. Search \n ")
    option=int(input("Enter the option ,creation must be done at 1st :"))
    if option==0:
        print("Thank you...")
    elif option==1:
        create_linkedlist()
    elif option==2:
        llist.traverse()
    elif option==3:
        print("...Please select where to insert the number...")
        print(" 1.Insertion_at_front \n 2.insertion_at_particular point \n 3.insertion_at_end")
        choice=int(input("\nEnter the choice :"))
        if choice == 1:
           llist.insertion_at_front()
        elif choice == 2:
            llist.insertion_at_particular()
        elif choice == 3:
            llist.insertion_at_end()
    elif option==4:
        print("...Please select which element to delete...")
        print(" 1.Deletion_at_front \n 2.Deletion_at_particular point \n 3.Deletion_at_end")
        choice=int(input("\nEnter the choice :"))
        if choice == 1:
           llist.deletion_at_front()
        elif choice == 2:
            llist.deletion_at_particular()
        elif choice == 3:
            llist.deletion_at_end()
    
    elif option==5 :
            llist.search()
    else:
        print(" wrong option ... plss check again ...")
        main()

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
            print(t.data,end=" ")
            t=t.next
        print("\n")
        main()
# insertion in linkedlist at fornt of the linked list..
    
    def insertion_at_front(self):
        t=self.head
        newnode=node(int(input("enter a element to add at front :")))
        newnode.next=self.head
        self.head=newnode
        #self.head.next=t
        print(" insertion_at_front successfully..")
        main()
        
        #if int(input("want to traverse (1/0)"))==1:
        #   self.traverse()
        #else:
        #   print(" thank you ..")
      
    # add function just push the elemrnt in the linkedlist eventhough it not created..
    
    def add(self,data):
        if self.head==None:
            self.head=node(data)
        else:
            temp=self.head
            while temp.next!=None:
                temp=temp.next
            temp.next=node(data)
            
     # find the length of the linkedlist .. 
    
    def length(self):
        temp=self.head
        count=0
        while temp:
            count+=1
            temp=temp.next
        print(count," length..")
        
#insertion_at_end 
    
    def insertion_at_end(self):
        t=self.head
        while t.next!=None:
            t=t.next
        t.next=node(int(input("enter a element to add at end :")))
        #self.traverse()
        main()
        
 #reverse the linked list ..

    def reverse(self):
        pre=None
        current=self.head
        while current:
            next_node=current.next
            current.next=pre
            pre=current
            current=next_node
        self.head=pre
        
#insertion_at_particular point ..

    def insertion_at_particular(self):
        note_point=int(input(" enter the node point to add: "))
        temp=self.head
        for i in range(note_point-1):
            temp1=temp
            temp=temp.next
        adss=temp1.next
        temp1.next=node(int(input(" enter the num for new node :")))
        temp1.next.next=adss
        main()
        #self.traverse()
 
#search element in the linkedlist 

    def search(self):
        temp=self.head
        element_to_search=int(input("enter the element_to_search : "))
        i=1
        flag=True
        while temp!=None:
            if temp.data == element_to_search:
                print(temp.data," is found at ",i,"th node..",temp.next)
                flag=False
                break
            
            temp=temp.next
        if flag:
            print(" element is not founded ..")
            #self.traverse()
        main()
        
#deletion at front of linked list

    def deletion_at_front(self):
        temp=self.head
        self.head=temp.next
        temp.next=None
        print("The element at front of the list is deleted...")
        main()
        
#deletion at end of the list

    def deletion_at_end(self):
        temp=self.head.next
        prev=self.head
        while temp.next is not  None:
            temp=temp.next
            prev=prev.next
        prev.next=None
        print("The element at end of the list is FDeleted...")
        main()
        
#deletion at particular point

    def deletion_at_particular(self):
        temp=self.head.next
        prev=self.head
        node_point=int(input("Enter the position of the element to delete..."))
        for j in range(1,(node_point)-1):
            temp=temp.next
            prev=prev.next
        prev.next=temp.next
        temp.next=None
        print("The element at particular point Deleted...")
        main()
        
  #deletion at front by msbala

   def delete_at_front(self):
        temp=self.head
        self.head=self.head.next
        print(temp.data," was deleted ...")
        temp.next=None
        
  #by msbala del at end 
    
    def delete_at_end(self):
        temp=self.head
        while temp.next!=None:
            pre=temp
            temp=temp.next
        print(temp.data," was deleted ...")
        pre.next=None
        
    #this deletion using key or element  .. 
    
    def delete_using_key(self,data):
        temp=self.head
        if temp.data!=data:
            t=True
            while temp!=None:
                # pre=temp
                if temp.next==None:
                    temp=temp.next
                    break
                if temp.next.data==data:
                    break
                temp=temp.next
            if temp==None:
                print("element is not found to delete..")
            else:
                linking=temp.next.next
                temp.next.next=None
                print("deleted successfully..")
                temp.next=linking
        else:
            self.delete_at_front()
                       
            

#when i create obj for this class , it create a head = none

llist=linked() 

#linkedlist create code wrap in the function..

def create_linkedlist():
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
        #if int(input(" want to traverse :(1/0)"))==1:
         #   llist.traverse()
        #else:
         #   print(" thank you ...")
        main()
# create_linkedlist()     
# llist.insertion_at_front()
# llist.insertion_at_end()
# llist.insertion_at_particular()
# llist.search()
main()

