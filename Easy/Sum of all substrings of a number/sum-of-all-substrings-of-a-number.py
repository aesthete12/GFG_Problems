#User function Template for python3

class Solution:
    # Function to find sum of all possible substrings of the given string.
    def sumSubstrings(self, s):
        MOD = 10**9 + 7
        n = len(s)
        
        # Initialize variables to store the result and the current value.
        result = 0
        current_value = 0
        
        # Loop through the string from left to right.
        for i in range(n):
            # Update the current value by multiplying it by 10 and adding the current digit.
            current_value = (current_value * 10 + int(s[i]) * (i + 1)) % MOD
            
            # Add the current value to the result.
            result = (result + current_value) % MOD
        
        # Return the final result.
        return result

#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

import sys
sys.setrecursionlimit(10**6)

# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        s = str(input())
        ob=Solution()
        print(ob.sumSubstrings(s))
# } Driver Code Ends