#User function Template for python3

class Solution:
    def reversedBits(self, x):
        result = 0
        for i in range(32):
            if x & 1:
                result |= 1 << (31 - i)
            x >>= 1
        return result

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        X=int(input())
        
        ob = Solution()
        print(ob.reversedBits(X))
# } Driver Code Ends