#User function Template for python3
class Solution:
    # Function to check if given number n is a power of two.
    def isPowerofTwo(self, n: int) -> bool:
        # If n is less than or equal to 0, it cannot be a power of 2
        if n <= 0:
            return False
        
        # Using bitwise AND operation to check if n is a power of 2
        # A power of 2 has only one bit set in its binary representation
        # So, if n & (n - 1) is 0, it means n has only one bit set
        return n & (n - 1) == 0
#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math


def main():
    
    T=int(input())
    
    while(T>0):
        
        
        n=int(input())
        ob=Solution()
        if ob.isPowerofTwo(n):
            print("YES")
        else:
            print("NO")
        
        T-=1

if __name__=="__main__":
    main()
# } Driver Code Ends