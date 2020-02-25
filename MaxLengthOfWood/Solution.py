


import os 
import sys 
import math


class Solution:

    def __init__(self):
        pass 

    def solution(self, dividends:[], k:int):
        ## Set the divisor to largest dividend +1
        dividends.sort(reverse=True)
        divisor = dividends[0]+1
        ##while the sum of the quotients is lesss than k
        ##continue to reduce the divisor
        while(self.sumOfQuotients(dividends, divisor) < k):
            divisor -= 1

        ##the divisor is the maximal length of each sub-piece of wood such that K sub-pieces of wood were made        
        return divisor

    ##return the sum of qutients
    def sumOfQuotients(self, arr, divisor):
        sum = 0
        ##for each dividiend in the arry
        for dividend in arr:
            ##take the floor of the dividend divided by the divisor and add it to the sum 
            sum += math.floor(dividend/divisor)
    
        ##return the sum
        return sum


if __name__ == "__main__":
    l = [232, 124, 456]
    k = 7
    s = Solution()
    print(s.solution(l, k))