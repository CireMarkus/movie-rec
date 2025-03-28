from Node import Node
class Tree: 
    def __init__(self,root = None):
        if type(root) == Node:
            self.root = root
        else:
            self.root = Node(root)
    
   
    
    def add_node(self,node):
        #function to add a node to the tree
        new_node =  node
        current_node = self.root
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
        #function to traverse the tree and print the tree. 
        needtovisit = []
        needtovisit.append(self.root)

        while needtovisit: 
            current_node = needtovisit.pop(0)
            if current_node.getLeft() or current_node.getRight():
                if current_node.getLeft():
                    needtovisit.append(current_node.getLeft())
                if current_node.getRight():
                    needtovisit.append(current_node.getRight())
            print(current_node.getData())
            
    def search(self,value):
        
        pass

    def inorder_trav(self):
        
        pass
    def preorder_trav(self):
        pass
    def postorder_trav(self):
        pass

node1 = Node(12)
node2 = Node(14)
node3 = Node(11)
node4 = Node(55)




tree1 = Tree(node1)

tree1.add_node(node2)
tree1.add_node(node3)
tree1.add_node(node4)
tree1.print_tree()



            
            
              
    