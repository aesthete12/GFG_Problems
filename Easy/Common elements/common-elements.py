#User function Template for python3
class Solution:
    def commonElements(self, A, B, C, n1, n2, n3):
        # Initialize pointers for each array
        i, j, k = 0, 0, 0
        result = []
        prev = None  # Variable to keep track of previously found common element

        # Iterate through all three arrays
        while i < n1 and j < n2 and k < n3:
            # If elements are equal and not equal to the previous common element
            if A[i] == B[j] == C[k] and A[i] != prev:
                result.append(A[i])
                prev = A[i]
                i += 1
                j += 1
                k += 1
            # If A[i] is smaller, move pointer i
            elif A[i] < B[j] or A[i] < C[k]:
                i += 1
            # If B[j] is smaller, move pointer j
            elif B[j] < A[i] or B[j] < C[k]:
                j += 1
            # If C[k] is smaller, move pointer k
            else:
                k += 1

        return result
#{ 
 # Driver Code Starts
#Initial Template for Python 3


t = int (input ())
for tc in range (t):
    n1, n2, n3 = list(map(int,input().split()))
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    C = list(map(int,input().split()))
    
    ob = Solution()
    
    res = ob.commonElements (A, B, C, n1, n2, n3)
    
    if len (res) == 0:
        print (-1)
    else:
        for i in range (len (res)):
            print (res[i], end=" ")
        print ()

# } Driver Code Ends