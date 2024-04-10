#User function Template for python3

class Solution:
    ##Complete this function
    # function to convert a given Gray equivalent n to Binary equivalent.
    def grayToBinary(self, n):
        # Gray to binary conversion algorithm:
        # Start with the most significant bit (MSB) of the Gray code, which is the same as the binary code.
        # XOR each bit of the Gray code with the previous bit of the Gray code to get the corresponding binary bit.
        # Initialize the result with the MSB of the Gray code.
        result = n
        
        # Iterate from the next bit to the least significant bit (LSB).
        while n > 0:
            n >>= 1  # Right shift to move to the next bit.
            result ^= n  # XOR with the shifted value.
        
        # The result now holds the binary equivalent of the Gray code.
        return result

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math


def main():
    
    T=int(input())
    
    while(T>0):
        
        
        n=int(input())
        ob=Solution()
        print(ob.grayToBinary(n))
        T-=1

if __name__=="__main__":
    main()
# } Driver Code Ends