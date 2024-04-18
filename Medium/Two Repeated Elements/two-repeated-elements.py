#User function Template for python3

class Solution:
    def twoRepeated(self, arr , n):
        temp = {}
        ans,count = [],0
        for i in arr:
            if count==2:
                break
            temp[i] = temp.get(i,0)+1
            if temp[i]==2:
                ans.append(i)
                count+=1
        return ans
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
            ans = obj.twoRepeated(A,N)
            print(ans[0], ans[1])
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends