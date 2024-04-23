#User function Template for python3
class Solution:
    def firstElement (self, n):
        # code here 
        import numpy as np
        a = np.array([[1, 1], [1, 0]])
        ans = np.array([[1, 0], [0, 1]])
        M = 1000000007
        while n > 0:
            if n&1 == 1:
                ans = ans@a%M
            a = a@a%M
            n >>= 1
        return ans[1][0]    


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        n = int(input())
        
        ob = Solution()
        print(ob.firstElement(n))
# } Driver Code Ends