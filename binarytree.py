class BinaryTree:

    def __init__(self, data):
        self.flag= False
        self.left = None
        self.right = None
        self.data = data

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
# root.insert(55)
# root.insert(60)
# root.insert(20)
# root.insert(52)

root.PrintTree()
root.search(int(input(" enter a element to search :")))
# if root.flag:
#     Print("not found ..")
