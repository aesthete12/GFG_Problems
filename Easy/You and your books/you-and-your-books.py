
class Solution:
    #Your task is to complete this function
    #Function should return an integer
    #a - list/array containing height of stack's respectively
    def max_Books(self, n, k, arr):
        #code here
        s=0
        m=0
        i=0
        while(i!=n):
            if arr[i]>k:
                i+=1
                m=max(m,s)
                s=0
            else:
                s+=arr[i]
                i+=1
        return max(m,s)

#{ 
 # Driver Code Starts
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        temp = list(map(int, input().strip().split()))
        n = temp[0]
        k = temp[1]
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.max_Books(n, k, arr))
# Contributed by:Harshit Sidhwa

# } Driver Code Ends