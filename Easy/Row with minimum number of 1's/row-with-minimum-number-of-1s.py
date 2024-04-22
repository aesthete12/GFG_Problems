#User function Template for python3

class Solution:
    def minRow(self,n,m,a):
        #code here
        
        d={i:0 for i in range(1,n+1)}
        for i in range(n):
            temp=a[i].count(1)     
            d[(i+1)]=temp
        min_v=min(d.values())
        min_k=[k for k,v in d.items() if v==min_v]
        return min(min_k)

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math
        
if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        N,M=map(int,input().strip().split(" "))
        A=[]
        for i in range(N):
            B=list(map(int,input().strip().split(" ")))
            A.append(B)
        ob=Solution()
        print(ob.minRow(N,M,A))
# } Driver Code Ends