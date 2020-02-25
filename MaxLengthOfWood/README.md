## Given an array of length N, each index in the array, a[i] represents the length of a piece of wood.
## Given K > N, the question asks you to make K smaller pieces of wood of maximal length from the original N pieces of wood.
## For example if N = 3, K = 4, arr = [2, 3, 4] then the maxmimal length of the 4 smaller pieces of wood is 2.


## Algorithm
## while(floor(arr[0]/count + ...  floor(arr[i])/count + ...floor(arr[n])/count > K)
## count ++

