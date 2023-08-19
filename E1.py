# check 'QuestionList' file for the question
# * Source : GFG
   
class Solution:
    def leaders(self, A, N):
       
        leader = []
     #   leader.append(A[-1])    #last most always a leader
        maxRight = A[N-1]

        #for i in A[-2::-1]:
         
        for i in range(N - 2, -1, -1):
            if A[i] >= maxRight :   # second last > last ~ second largest is a leader
             maxRight = A[i]
             leader.append(maxRight)
        leader = leader[::-1]
        leader.append(A[-1])     
        return leader
        
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math


    
def main():
    
    T=int(input())
    
    while(T>0):
        
        
        N=int(input())
        
        A=[int(x) for x in input().strip().split()]
        obj = Solution()
        
        A=obj.leaders(A,N)
        
        for i in A:
            print(i,end=" ")
        print()
        
        T-=1

if __name__=="__main__":
    main()
# } Driver Code Ends