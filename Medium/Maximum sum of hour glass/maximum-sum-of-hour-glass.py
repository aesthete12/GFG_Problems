#User function Template for python3

class Solution:
    def findMaxSum(self,n,m,mat):
        if len(mat) < 3:
            return -1
        hourglass = []
        for i in range(n):
            if i-1 >=0 and i+1 < n:
                res = 0
                for j in range(m):
                    if j-1 >=0 and j+1 < m:
                        res = mat[i][j] + mat[i-1][j-1] + mat[i-1][j] + mat[i-1][j+1] + mat[i+1][j-1] + mat[i+1][j] + mat[i+1][j+1]
                        hourglass.append(res)
        return max(hourglass)

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math
      
if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        N,M=map(int,input().strip().split(" "))
        Mat=[]
        for i in range(N):
            B=list(map(int,input().strip().split(" ")))
            Mat.append(B)
        ob=Solution()
        ans=ob.findMaxSum(N,M,Mat)
        print(ans) 
# } Driver Code Ends