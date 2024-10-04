class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
class binarytree:
    def __init__(self,data):
        self.root=Node(data)
    def insert(self,data):
        newnode=Node(data)
        if self.root== None:
            self.root=newnode
            return
        queue=[self.root]
        while queue:
            temp=queue.pop(0)
            if (temp.left==None):
               temp.left=newnode
               break
            else:
               queue.append(temp.left)
            if(temp.right==None):
               temp.right=newnode
               break
            else:
              queue.append(temp.right)
    def inorder(self,node):
        if node:
            self.inorder(node.left)
            print(node.data,end=" ")
            self.inorder(node.right)
    
    def preorder(self,node):
        if node:
            print(node.data,end=" ")
            self.preorder(node.left)
            self.preorder(node.right)
            
    def postorder(self,node):
        if node:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.data,end=" ")
            
n=int(input())
tree=binarytree(n)
m=int(input())
for i in range(m):
    s=int(input())
    tree.insert(s)
tree.inorder(tree.root)
tree.preorder(tree.root)
tree.postorder(tree.root)
        
