import os
import sys


class Solution:

    def __init__(self):
        pass

    def solution(self, points:[[]])->int:

        max = 2
        curMax = 2
        startingPoint = points[0]
        
        ##starting point is point at 0.
        ##since all other points can make a line with starting point 
        ##keep in constant
        for i in range(1, len(points)-1):
            ##get the slope and y intercept using starting point and current point at i
            slope = self.getSlope(startingPoint, points[i])
            yInt = self.getYIntercept(startingPoint, slope)
            ## check the remaing points and see if they are on the line formed by starting point and current point
            for j in range(i+1, len(points)):
                newPoint = points[j]
                ##this is where the check occurrs
                if newPoint[1] == slope*newPoint[0] + yInt:
                    curMax += 1
            
            if curMax > max:
                max = curMax
            curMax = 0
        
        return max

    ##calculate Y intercept
    def getYIntercept(self, point:[], slope:float)->float:
        return point[1] - (point[0]*slope)

    ##calculate slope
    def getSlope(self, p1:[], p2:[])->float:
        return (p2[1] - p1[1])/(p2[0] - p1[0])
    


if __name__ == "__main__":

    
    points = []
    fName = sys.argv[1]
    fileObj = open(fName, "r")
    for line in fileObj:
        point = line.split() 
        point[0], point[1] = int(point[0]), int(point[1])
        points.append(point)


    fileObj.close()
    s = Solution()
    print(s.solution(points))
