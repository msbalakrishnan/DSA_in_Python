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

