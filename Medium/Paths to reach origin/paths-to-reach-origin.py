#User function Template for python3

class Solution:
    def ways(self, n,m):
        #write you code here
        ans = 1
        for i in range(1,m+1):
            ans = ans * (m+n+1-i)//(i)
        return ans%1000000007

#{ 
 # Driver Code Starts
#Initial Template for Python 3

t=int(input())
for _ in range(0,t):
    x,y=list(map(int,input().split()))
    ob = Solution()
    print(ob.ways(x,y))
# } Driver Code Ends