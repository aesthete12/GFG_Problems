class Solution:
    def countWays(self, s1 : str, s2 : str) -> int:
        # code here
        MOD=10**9+7
        n= len(s1)
        m=len(s2)
        
        d=[[0]*(n+1) for _ in range (m+1)]
        for j in range(n+1):
            d[0][j]=1
        for i in range(1,m+1):
            for j in range(1,n+1):
                if s2[i-1]==s1[j-1]:
                    d[i][j]=(d[i-1][j-1]+d[i][j-1])%MOD
                else:
                    d[i][j]=d[i][j-1]
                    
        return d[m][n]


#{ 
 # Driver Code Starts
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):

        s1 = (input())

        s2 = (input())

        obj = Solution()
        res = obj.countWays(s1, s2)

        print(res)

# } Driver Code Ends