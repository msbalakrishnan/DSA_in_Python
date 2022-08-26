#perform out side of the class or right way to insert
class bst:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
# code for insertion ...
def insert(root,key):
    if root:
        if root.data<key:
            root.right=insert(root.right,key)
        else:
            root.left=insert(root.left,key)
    else:
        root=bst(key)
    return root

#finding the min element in the tree, infact it is left most element 

def minkey(root):
    if root==None:
        return None
    
    while root:
        pre=root
        root=root.left
    return pre

#this code for deletion in the three case 
# refer here for more information ..
#'''https://www.techiedelight.com/deletion-from-bst/'''

def deletion(root,key):
    
    parent=None
    curr=root
    while curr and curr.data!=key:
        parent=curr
        if curr.data>key:
            curr=curr.left
        else:
            curr=curr.right
    # if the element is not found ...
    if curr==None:
        return root
    if curr.left==None and curr.right==None:
        if curr!=root:
            if parent.left==curr:
                parent.left=None
            else:
                parent.right=None
        else:
            return None
    elif curr.left and curr.right:
        #finding alternate node 
        var=minkey(curr.right).data
        #var=6
        
        deletion(root,var)
        curr.data=var
        
    else:
        if curr.left:
            child=curr.left
        else:
            child=curr.right
        if curr!=root:
            if parent.left==curr:
                parent.left=child
            else:
                parent.right=child
        else:
            root=child
    return root
        
                
 # finfin the max element in the tree , infact it is right most element ..


def maxkey(root):
    if root==None:
        return None
    while root:
        pre=root
        root=root.right
    return pre
   

def inorder(root):
    #simillarly for pre ,post 
    if root==None:
        return 
        
    inorder(root.left)
    print(root.data)
    inorder(root.right)

        
root=None

for i in range(int(input("enter how many element you want : "))):
    root=insert(root,int(input("enter the element : ")))
else:
    print("successfully created ...")
    
print("inorder traversal .. ")

inorder(root)
print("find the minimum element in the tree ")
r=minkey(root)
if r:
    print(" the minimum element is ",r.data)
else:
    print("the tree is empty  ...")
print("find the minimum element in the tree ")
r=maxkey(root)
if r :
    print("max element is ",r.data)
else:
    print(" the tree is empty ..")
    
#calling a deletion here..  
root=deletion(root,int(input("enter element to deletion : ")))

inorder(root)

# create the class with constructor to create a node element 

class BinaryTree:

    def __init__(self, data):
        self.flag= False
        self.left = None
        self.right = None
        self.data = data
        
# code for insertion in binary tree , basically binary  tree contructed based by BST 
    
    def insert(self, data):

        if self.data:
            if data < self.data:
                if self.left is None:
                    
                    self.left = BinaryTree(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = BinaryTree(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data
           
    # good to refer the another another search code because it contain erro so i used the try block . but it running good 
    
    def search(self,data):
     try:
        self.flag=False
        if self.data:
            if self.data==data:
                
                
                print(" found at root ")
                flag=True
            elif data< self.data :
                self.left.search(data)
            elif data> self.data:
                self.right.search(data)
            
     except:
         print("element is not found")
            
     # print the inorder traversal of the binay tree ( left-data-right)
    
        
    def inorder_traverse(self,root):
        if root:
            root.inorder_traverse(root.left)
            print(root.data,end=" ")
            root.inorder_traverse(root.right)
            
    # print the preorder traversal of the binay tree ( data-left-right)
            
    def pre_order_traversal(self,root):
        if root:
            print(root.data,end=" ")
            root.pre_order_traversal(root.left)
            root.pre_order_traversal(root.right)
            
   # print the post order traversal of the binay tree ( left-right-data)
            
    def post_order_traversal(self,root):
        if root:
            root.post_order_traversal(root.left)
            root.post_order_traversal(root.right)
            print(root.data,end=" ")    
        
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print( self.data),
        if self.right:
            self.right.PrintTree()

for i in range(int(input("enter how many number you want : "))):
     if i ==0:
        root = BinaryTree(int(input("enter the root element :")))
     else:
        root.insert(int(input(" enter the element: ")))

root.PrintTree()
root.search(int(input(" enter a element to search :")))

