#User function Template for python3

class Solution:
    # Function to check whether two strings are anagrams of each other or not.
    def isAnagram(self, a, b):
        # Dictionary to store frequency of characters in string a
        count_a = {}
        # Dictionary to store frequency of characters in string b
        count_b = {}
        
        # Count frequency of characters in string a
        for char in a:
            count_a[char] = count_a.get(char, 0) + 1
        
        # Count frequency of characters in string b
        for char in b:
            count_b[char] = count_b.get(char, 0) + 1
        
        # Check if both dictionaries are equal
        return count_a == count_b

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        a,b=map(str,input().strip().split())
        if(Solution().isAnagram(a,b)):
            print("YES")
        else:
            print("NO") 
# } Driver Code Ends