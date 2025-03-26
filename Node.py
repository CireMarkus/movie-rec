class Node:
    def __init__(self,data):
        self.data = data
        self.left = None 
        self.right = None
    
    def setLeft(self,node):
        self.left = node
    
    def setRight(self,node):
        self.right = node
        
    def getleft(self):
        return self.left
    
    def getright(self):
        return self.right
    
    
        