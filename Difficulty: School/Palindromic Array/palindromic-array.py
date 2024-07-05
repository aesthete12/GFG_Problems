# Your task is to complete this function
# Function should return 1/0
def is_palindrome(num):
    # Convert the number to string and check if it reads the same forward and backward
    return str(num) == str(num)[::-1]

def PalinArray(arr):
    for num in arr:
        if not is_palindrome(num):
            return 0
    return 1


#{ 
 # Driver Code Starts
# Driver Program
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        arr = list(map(int, input().strip().split()))
        if PalinArray(arr):
            print(1)
        else:
            print(0)
# Contributed By: Harshit Sidhwa

# } Driver Code Ends