#User function Template for python3
class Solution:
    def getPairsCount(self, arr, n, k):
        # Dictionary to store the frequency of each element
        freq_map = {}
        count_pairs = 0
        
        # Count the frequency of each element
        for num in arr:
            if num in freq_map:
                freq_map[num] += 1
            else:
                freq_map[num] = 1
        
        # Iterate through the array
        for num in arr:
            # Calculate the complement
            complement = k - num
            # If the complement exists in the dictionary
            if complement in freq_map:
                # If num and complement are the same, we need to count the pairs correctly
                if num == complement:
                    count_pairs += freq_map[num] - 1
                else:
                    count_pairs += freq_map[complement]
        
        # Return the total count of pairs
        return count_pairs // 2  # Since each pair is counted twice
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n, k = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.getPairsCount(arr, n, k)
        print(ans)
        tc -= 1

# } Driver Code Ends