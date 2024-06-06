# your task is to complete this function
# function should return index to the any valid peak element
class Solution:   
    def peakElement(self,arr, n):
        # Code here
        result = []
        for i in range(n):
            if i==0:
                left = None
            else:
                left = arr[i-1]
            if i==n-1:
                right = None
            else:
                right = arr[i+1]
                
            if left==None and right==None:
                result.append(i)
            elif left==None and right!=None:
                if arr[i]>=right:
                    result.append(i)
            elif left!=None and right!=None:
                if arr[i]>=left and arr[i]>=right:
                    result.append(i)
            elif left!=None and right==None:
                if arr[i]>=left:
                    result.append(i)
            else:
                print("Hi hI hI...")
        return result[0]


#{ 
 # Driver Code Starts

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        index = Solution().peakElement(arr.copy(), n)
        flag = False
        if index<0 or index>=n:
            flag = False
        else:
            if index == 0 and n==1:
                flag = True
            elif index==0 and arr[index]>=arr[index+1]:
                flag = True
            elif index==n-1 and arr[index]>=arr[index-1]:
                flag = True
            elif arr[index-1] <= arr[index] and arr[index] >= arr[index+1]:
                flag = True
            else:
                flag = False

        if flag:
            print(1)
        else:
            print(0)
# Contributed by: Harshit Sidhwa

# } Driver Code Ends