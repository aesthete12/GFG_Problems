#User function Template for python3

class Solution:
    def pairAndSum(self, n, arr):
        total_sum = 0  # Initialize the total sum
        max_bit_length = max(arr).bit_length()  # Get the number of bits in the largest number
        
        # Iterate through each bit position from right to left
        for bit_position in range(max_bit_length):
            count = 0  # Initialize the count of pairs where both corresponding bits are 1
            
            # Iterate through each element in the array
            for num in arr:
                # Check if the bit at the current position is 1
                if (num >> bit_position) & 1:
                    count += 1  # Increment count if the bit is 1
            
            # Calculate the sum contribution of current bit position and add it to total_sum
            total_sum += (count * (count - 1)) // 2 * (1 << bit_position)
        
        return total_sum

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        N=int(input())
        Arr=list(map(int,input().strip().split(' ')))
        ob=Solution()
        print(ob.pairAndSum(N,Arr))
# } Driver Code Ends