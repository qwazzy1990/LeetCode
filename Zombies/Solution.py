import os
import sys

class Node:
    
    def __init__(self, val):
        self.val = val
        self.flipped = False
    
class Solution:

    def __init__(self):
        self.world = []
        self.startRow = -1
        self.startCol = -1
        self.count = 0

    ##create the world from the file
    def createWorld(self, fileName):
        file = open(fileName, "r")

        for line in file:
            node = Node(-1)
            node.flipped = True
            line = str(line).rstrip()
            arr = []
            arr.append(node)
            for i in range(0, len(line)):
                node = Node(int(line[i]))
                if node.val == 1:
                    node.flipped = True
                arr.append(node)
        
            node = Node(-1)
            node.flipped = True
            arr.append(node)
            self.world.append(arr)
        
        temp = []
        for i in range(len(self.world[0])):
            node = Node(-1)
            node.flipped = True
            temp.append(node)
        
        self.world.insert(0, temp)
        self.world.append(temp)
        self.printWorld()


    ##once world is created find the first '1' in the world and return its row and column
    
    def findFirstOne(self):
        for i in range(len(self.world)):
            for j in range(len(self.world[0])):
                if self.world[i][j].val == 1:
                    self.startRow = i
                    self.startCol = j
                    return 


    ##main driver, recursive
    def driver(self):
        
        if self.zombified():
            return

        
        self.count += 1


        for row in range(0, len(self.world)):
            for col in range(0, len(self.world[0])):
                if self.world[row][col].val == 1:
                    a = self.flipNeighbors(row-1, col)
                    b = self.flipNeighbors(row, col+1)
                    c = self.flipNeighbors(row+1, col) 
                    d = self.flipNeighbors(row, col-1)
        

        for i in range(0, len(self.world)):
            for j in range(0, len(self.world[0])):
                if self.world[i][j].flipped == True and self.world[i][j].val == 0:
                    self.world[i][j].val = 1
    

        if self.zombified():
            return
        else:
            self.driver()
    
    
    def flipNeighbors(self, row, col)->bool:

        ##flip upper neighbor

        if self.world[row][col].flipped == False:
            self.world[row][col].flipped = True
            return True

        return False

    def zombified(self)->bool:
        for i in range(len(self.world)):
            for j in range(len(self.world[0])):
                if self.world[i][j].val == 0:
                    return False
        
        return True

    def allHumans(self)->bool:
        for i in range(len(self.world)):
            for j in range(len(self.world[0])):
                if self.world[i][j].val == 1:
                    return False
        
        return True

    def printWorld(self):
        for i in range(0, len(self.world)):
            for j in range(0, len(self.world[0])):
                print("("+str(self.world[i][j].val) + " " + str(self.world[i][j].flipped) + ")", end = '')
            
            print()

if __name__ == "__main__":
    s = Solution()
    s.createWorld(sys.argv[1])
    s.findFirstOne()
    s.driver()
    print(s.count)
    s.printWorld()