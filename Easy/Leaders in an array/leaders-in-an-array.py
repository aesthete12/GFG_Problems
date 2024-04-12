
class Solution:
    #Function to find the leaders in the array.
    def leaders(self, A, N):
        leaders_list = []
        max_right = float('-inf')  # Initialize max_right as negative infinity
        
        # Traverse the array from right to left
        for i in range(N - 1, -1, -1):
            if A[i] >= max_right:  # Check if the current element is greater than or equal to max_right
                leaders_list.append(A[i])  # If yes, it's a leader
                max_right = A[i]  # Update max_right
        
        # Reverse the leaders_list to maintain the order of appearance
        return leaders_list[::-1]

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math


    
def main():
    
    T=int(input())
    
    while(T>0):
        
        
        N=int(input())
        
        A=[int(x) for x in input().strip().split()]
        obj = Solution()
        
        A=obj.leaders(A,N)
        
        for i in A:
            print(i,end=" ")
        print()
        
        T-=1

if __name__=="__main__":
    main()
# } Driver Code Ends