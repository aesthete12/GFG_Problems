#User function Template for python3

#Function to find the maximum possible amount of money we can win.

class Solution:
    def optimalStrategyOfGame(self, n, arr):
        # Creating a 2D DP table
        dp = [[0] * n for _ in range(n)]

        # Filling the DP table diagonally
        for gap in range(n):
            for i in range(n - gap):
                j = i + gap
                x = 0 if (i + 2) > j else dp[i + 2][j]
                y = 0 if (i + 1) > (j - 1) else dp[i + 1][j - 1]
                z = 0 if i > (j - 2) else dp[i][j - 2]

                dp[i][j] = max(arr[i] + min(x, y), arr[j] + min(y, z))

        # The maximum amount user can win is stored at dp[0][n-1]
        return dp[0][n - 1]
        
#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        arr = list(map(int,input().strip().split()))
        ob = Solution()
        print(ob.optimalStrategyOfGame(n,arr))

# } Driver Code Ends