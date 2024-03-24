# User function Template for python3

class Solution:
    def reverseWords(self, S):
        words = S.split('.')
        reversed_words = reversed(words)
        return '.'.join(reversed_words)

#{ 
 # Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        s = str(input())
        obj = Solution()
        print(obj.reverseWords(s))

# } Driver Code Ends