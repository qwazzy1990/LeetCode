import os 
import sys 




class Node:
    
    def __init__(self, val):
        self.val = val
        self.leftChild = None
        self.rightChild = None 
    

class Tree:

    def __init__(self):
        self.root = None
        self.numNodes = 0


    ##insert a new node
    def insert(self, node, val):

        ##if there are no nodes in the tree
        if self.numNodes == 0:
            self.root = Node(val)
            self.numNodes += 1
            return 

        if node.leftChild == None and val <= node.val:
            node.leftChild = Node(val)
            self.numNodes+= 1
            return
        if node.rightChild == None and val >= node.val:
            node.rightChild = Node(val)
            self.numNodes += 1
            return

        if val < node.val:
            self.insert(node.leftChild, val)        

        if val >= node.val:
            self.insert(node.rightChild, val)


    ##remove a node
    def remove(self, node, val):
        ##if cannot go further down the tree and no node was found
        if node == None:
            return
        ##if the value is in the right part of the tree
        if node.val < val:
            self.remove(node.rightChild, val)

        ##if the value is in the left subtree
        if node.val > val:
            self.remive(node.leftChild, val)        

        ##if the node's value = val then remove it
        if node.val == val:
            ##if the node has no children, ie. it is a leaf node then
            if node.leftChild == None and node.rightChild == None:
                node = None
                self.numNodes -= 1
                return   
            
            ##if the node only has one child, swap the node with its existing child and free
            if node.leftChild != None and node.rightChild == None:
                node.val = node.leftChild.val
                node.leftChild = None

                self.numNodes -= 1
                return
            
            ##if node has only left child
            if node.rightChild != None and node.leftChild == None:
                node.val = node.rightChild.val
                node.rightChild = None
                
                self.numNodes -= 1
                return
        
            ##last case, if node has two children
            if node.rightChild != None and node.leftChild != None:
                ##get the min value > than the value to be deleted
                minSuccessor = self.findMinSuccessor(node.rightChild)
                ##the node's val is this val
                node.val = minSuccessor.val
                ##now remove the minSuccessor
                self.remove(node.rightChild, minSuccessor.val)
                return

   
   
    ##finds the leftmost node in left subtree
   
    def findMinSuccessor(self, node):
        ##if at the last node in left subtree
        if(node.leftChild == None):
            return node
        
        ##else recursively call on left subtree
        return self.findMinSuccessor(node.leftChild)


    ##print the tree
    def printTree(self, node):
        if node == None:
            return
    
        print(node.val)
        self.printTree(node.leftChild)
        self.printTree(node.rightChild)


    def inOrder(self, node):
        ##if at a leaf
        if node.leftChild == None and node.rightChild == None:
            print(node.val)
            return node
        
        ##if at a non leaf with no left child
        elif node.leftChild == None and node.rightChild != None:
            print(node.val)
            rightChild = self.inOrder(node.rightChild)
            return rightChild

        else:
            leftChild = self.inOrder(node.leftChild)
            print(node.val)

            rightChild = self.inOrder(node.rightChild)
            ##print(rightChild.val)

if __name__ == "__main__":

    tree = Tree()
    tree.insert(tree.root, 5)
    tree.insert(tree.root, 3)
    tree.insert(tree.root, 9)
    tree.insert(tree.root, 11)
    tree.insert(tree.root, 4)
    tree.inOrder(tree.root)