class Solution:
    def findSwapValues(self,a, n, b, m):
        # Your code goes here
        a.sort()
        b.sort()
        diff=sum(b)-sum(a)
        if diff%2==1: return -1
        diff//=2
        i,j=0,0
        while b[j]-a[i]!=diff:
            if b[j]-a[i]<diff:
                j+=1
                if j>=m: return -1
            else:
                i+=1
                if i>=n: return -1
        return 1


#{ 
 # Driver Code Starts
if __name__ == '__main__': 
    
    
    t=int(input())
    for _ in range(0,t):
        l=list(map(int,input().split()))
        n=l[0]
        m=l[1]
        a = list(map(int,input().split()))
        b = list(map(int, input().split()))
        ob = Solution()
        print(ob.findSwapValues(a,n,b,m))
# } Driver Code Ends