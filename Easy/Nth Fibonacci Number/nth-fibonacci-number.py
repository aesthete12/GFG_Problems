
class Solution:
    def nthFibonacci(self, n: int) -> int:
        MOD = 1000000007
        if n <= 1:
            return n
        
        # Initialize the first two Fibonacci numbers
        fib = [0] * (n + 1)
        fib[1] = 1
        
        # Compute Fibonacci numbers up to nth
        for i in range(2, n + 1):
            fib[i] = (fib[i - 1] + fib[i - 2]) % MOD
        
        return fib[n]


#{ 
 # Driver Code Starts
if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        n = int(input())
        
        obj = Solution()
        res = obj.nthFibonacci(n)
        
        print(res)
        

# } Driver Code Ends