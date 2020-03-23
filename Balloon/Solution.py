import os 
import sys
from functools import cmp_to_key




def compare(a, b):
        if a.idx == b.idx:
            return 0 
        
        if a.idx < b.idx:
            return -1 
        
        if a.idx > b.idx:
            return 1

class MaxThree:

    def __init__(self, vall, indx):
        self.val = vall
        self.idx = indx

class Solution:

    def __init__(self):
        self.sum = 0
        pass 


    
    ##keeps track of the indecies of the maximal 
    ##3 elements in the array
    def findMaxThree(self, arr:[], maxThree:[], found:[]):

        ##if you got the three indecies to 
        if len(maxThree) == 3 or len(a) < 3:
            return

        index = -1
        max = -1
        for i in range(0, len(arr)):
            ##find the max value and index in the array
            if (arr[i] > max) and (not a[i] in found):
                max = arr[i]
                index = i
        
        ##append the max index to indecies
        maxThree.append(MaxThree(max, index))
        found.append(max)

        #recursive call
        self.findMaxThree(arr, maxThree, found)

    ##the main driving function
    def driver(self, a:[], maxThree:[]):
        
        print(self.sum)
        ##if all that is left in the array is the max three, and a[0], a[n-1]then process 
        ##the last three and return
        if len(a) == 5:
            self.processLastThree(a, maxThree)
            ##return
            return
        
        minVal = float("inf")
        minIdx = -1

        ##find the minumum value between a[1] and a[left index of the max three]
        for i in range(1, maxThree[0].idx):
            if a[i] < minVal:
                minVal = a[i]
                minIdx = i 
        
        if minIdx != -1:
            self.sum += a[minIdx-1]*a[minIdx]*a[minIdx+1]
            print(1, self.sum)
            a.remove(a[minIdx])
        
        
        
        ##update the indecies in maxThree
        for i in range(1, len(a)-1):
            for mt in maxThree:
                if a[i] == mt.val:
                    mt.idx = i
        
        
        minVal = float("inf")
        minIdx = -1


        ##find the minimum value between left and mid index
        ##remove the element
        for i in range(maxThree[0].idx+1, maxThree[1].idx):
            if a[i] < minVal:
                minVal = a[i]
                minIdx = i 
        
        ##update the sum
        ##remove the element
        if minIdx != -1:
            self.sum += a[minIdx-1]*a[minIdx]*a[minIdx+1]
            print(2, self.sum)
            a.remove(a[minIdx])
        ##update the indecies in maxThree
        
        for i in range(1, len(a)-1):
            for mt in maxThree:
                if a[i] == mt.val:
                    mt.idx = i

        ##redo the process for the mid and right idx
        minIdx = -1
        minVal = float("inf") 
        
        
        for i in range(maxThree[1].idx+1, maxThree[2].idx):
            if a[i] < minVal:
                minVal = a[i]
                minIdx = i 


        ##update the sum
        ##remove the element
        if minIdx != -1:
            self.sum += a[minIdx-1]*a[minIdx]*a[minIdx+1]
            print(3, self.sum)
            a.remove(a[minIdx])
        
        ##update the left and right indecies in maxThree
        for i in range(1, len(a)-1):
            for mt in maxThree:
                if a[i] == mt.val:
                    mt.idx = i
        
        

        ##redo the process for the right idx to end of the array
        minIdx = -1
        minVal = float("inf") 
        
        
        for i in range(maxThree[2].idx+1, len(a)-1):
            if a[i] < minVal:
                minVal = a[i]
                minIdx = i 


        ##update the sum
        ##remove the element
        if minIdx != -1:
            self.sum += a[minIdx-1]*a[minIdx]*a[minIdx+1]
            print(4, self.sum)
            a.remove(a[minIdx])
        
        ##update the left and right indecies in maxThree
        for i in range(1, len(a)-1):
            for mt in maxThree:
                if a[i] == mt.val:
                    mt.idx = i


        ##recursive call for the 
        self.driver(a, maxThree)

    
    
    
    ##process the max three values when they are beside each other
    def processLastThree(self, a:[], maxThree:[]):
        self.sum += maxThree[0].val*maxThree[1].val*maxThree[2].val


        self.sum+= maxThree[0].val * maxThree[2].val
        self.sum += maxThree[2].val

    
if __name__ == "__main__":

    a = [1, 2, 8, 3, 5, 10,6,1]
    maxThree = []
    found = []
    s = Solution()
    s.findMaxThree(a, maxThree, found)
    print(found)
    maxThree = sorted(maxThree, key=cmp_to_key(compare))
    for m in maxThree:
        print(m.idx)
    s.driver(a, maxThree)
    print(s.sum)
