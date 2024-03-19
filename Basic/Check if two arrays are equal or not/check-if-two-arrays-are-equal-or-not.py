#User function Template for python3

class Solution:
    # Function to check if two arrays are equal or not.
    def check(self, A, B, N):
        # Create dictionaries to store frequencies of elements
        freqA = {}
        freqB = {}
        
        # Count frequencies of elements in array A
        for num in A:
            freqA[num] = freqA.get(num, 0) + 1
        
        # Count frequencies of elements in array B
        for num in B:
            freqB[num] = freqB.get(num, 0) + 1
        
        # Check if frequencies are equal for each element
        for num in freqA:
            if num not in freqB or freqA[num] != freqB[num]:
                return False
        
        return True

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for tc in range(t):
        
        N=int(input())
        
        A = [int(x) for x in input().replace('  ',' ').strip().split(' ')]
        B = [int(x) for x in input().replace('  ',' ').strip().split(' ')]
        ob=Solution()
        if ob.check(A,B,N):
            print(1)
        else:
            print(0)
        
                
                
# } Driver Code Ends