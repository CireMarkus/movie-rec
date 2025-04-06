from Node import Node
from random import randint
class Tree: 
    def __init__(self,root = None):
        if type(root) == Node:
            self.root = root
        else:
            self.root = Node(root)
    
    def tree_trav(self,current_node,needtovisit):
        #function to traverse the tree
        if current_node.getLeft() or current_node.getRight():
            if current_node.getLeft():
                needtovisit.append(current_node.getLeft())
            if current_node.getRight():
                needtovisit.append(current_node.getRight())

    
    def add_node(self,node):
        #function to add a node to the tree
        new_node =  node
        current_node = self.root
        if self.root.data == None:
            self.root = new_node
            return
        if type(new_node) != Node:
            new_node = Node(new_node)
        assigned = False
        while not assigned: 
            if new_node.getData() < current_node.getData():
                if current_node.getLeft():
                    current_node = current_node.getLeft()
                else: 
                    current_node.setLeft(new_node)
                    assigned = True
            else: 
                if current_node.getRight():
                    current_node = current_node.getRight()
                else: 
                    current_node.setRight(new_node)
                    assigned = True
            
    def print_tree(self):
        #function to traverse the tree and print the tree. BFS
        needtovisit = []
        needtovisit.append(self.root)

        while needtovisit: 
            current_node = needtovisit.pop(0)
            self.tree_trav(current_node,needtovisit)
            print(current_node.getData())
            
    def search(self,value):
        #function to search for a value in the tree
        pass
    
    
    
    def inorder_trav(self,current_node):
        #function to traverse the tree in order left, root,right
        if current_node.getLeft():
            self.inorder_trav(current_node.getLeft())
        
        print(current_node.getData())
        
        if current_node.getRight():
            self.inorder_trav(current_node.getRight())
        
            
        
            
    def revorder_trav(self,current_node):
        #function to traverse the tree in reverse order right, root,left
        if current_node.getRight():
            self.revorder_trav(current_node.getRight())
        
        print(current_node.getData())    
        
        if current_node.getLeft():
            self.revorder_trav(current_node.getLeft())
            
        
        
        
        
        
    