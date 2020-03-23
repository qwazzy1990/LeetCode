The problem: given an array of N integers where a[0] = 1, a[n-1] = 1 and a [1...n-2] 1 <= a[k], <= 100, 
remove an element in the array, when done so multiply the element by its two adjacent neighbors. A[0]
and A[N-1] cannot be removed. Continue until only A[0] and A[n-1] remain. 
What is the maximum sum you can get by removing all the elements in the array.

E.G. 
A = [1, 3, 4, 2, 5, 1] 
 Remove '3' -> 1*3*4 = 12, A = [1,4,2,5,1]
 Remove '4' ->1*4*2= 8, A=[1,2,5,1]
 Remove '2' -> 1*2*5 = 10, A=[1,5,1]
 Remove '5'->1*5*1 = 5, A=[1,1]