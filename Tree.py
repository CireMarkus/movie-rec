from Node import Node
class Tree: 
    def __init__(self,root = None):
        if type(root) == Node:
            self.root = root
        else:
            self.root = Node(root)
    
   
    #while assigned is false
    #check and see if the new node is less than the current node
        #check if the left child is none
            #if none assign new node to left child and break out of loop
            #assigned  set true
        #else assign left child to current node
    #else new node is greater than the current node
        #check if the right child is none 
            # if none assign new_node to right child and break out of loop
            #assigned set true       
    def add_node(self,node):
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
            

    
    #pop the first node and assign to current_node 
    #check to see if the current node has any children
    #append children to need to visit
    #print the value of the current node
    def print_tree(self):
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
            

        

node1 = Node(12)
node2 = Node(14)
node3 = Node(11)
node4 = Node(55)




tree1 = Tree(node1)

tree1.add_node(node2)
tree1.add_node(node3)
tree1.add_node(node4)
tree1.print_tree()



            
            
              
    