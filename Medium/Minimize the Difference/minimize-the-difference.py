

class Solution:
    @staticmethod
    def minimizeDifference(n, k, arr):
        max_suffix = [0] * (n + 1)
        min_suffix = [0] * (n + 1)

        max_suffix[n] = float('-inf')
        min_suffix[n] = float('inf')
        
        max_suffix[n - 1] = arr[n - 1]
        min_suffix[n - 1] = arr[n - 1]
        
        for i in range(n - 2, -1, -1):
            max_suffix[i] = max(max_suffix[i + 1], arr[i])
            min_suffix[i] = min(min_suffix[i + 1], arr[i])
        
        max_prefix = arr[0]
        min_prefix = arr[0]
        
        min_diff = max_suffix[k] - min_suffix[k]
        
        for i in range(1, n):
            if i + k <= n:
                maxi = max(max_suffix[i + k], max_prefix)
                mini = min(min_suffix[i + k], min_prefix)
       
                min_diff = min(min_diff, maxi - mini)
                
                max_prefix = max(max_prefix, arr[i])
                min_prefix = min(min_prefix, arr[i])
            else:
                return min_diff
        return min_diff


#{ 
 # Driver Code Starts

class IntArray:
    def __init__(self) -> None:
        pass
    def Input(self,n):
        arr=[int(i) for i in input().strip().split()]#array input
        return arr
    def Print(self,arr):
        for i in arr:
            print(i,end=" ")
        print()


if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        n = int(input())
        
        
        k = int(input())
        
        
        arr=IntArray().Input(n)
        
        obj = Solution()
        res = obj.minimizeDifference(n, k, arr)
        
        print(res)
        

# } Driver Code Ends