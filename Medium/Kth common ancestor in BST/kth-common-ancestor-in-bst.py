#User function Template for python3

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Solution:
    def findPath(self, root, target, path):
        if root is None:
            return False
        path.append(root.data)

        if root.data == target:
            return True

        if (root.left and self.findPath(root.left, target, path)) or \
           (root.right and self.findPath(root.right, target, path)):
            return True

        path.pop()
        return False

    def kthCommonAncestor(self, root, k, x, y):
        path_x = []
        path_y = []

        if not self.findPath(root, x, path_x) or not self.findPath(root, y, path_y):
            return -1

        i = 0
        while i < len(path_x) and i < len(path_y):
            if path_x[i] != path_y[i]:
                break
            i += 1

        if i < k:
            return -1
        return path_x[i - k]

#{ 
 # Driver Code Starts

#Initial Template for Python 3


from collections import deque

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Function to Build Tree
def buildTree(str):
    # Corner Case
    if len(str) == 0 or str[0] == 'N':
        return None

    # Creating list of strings from input string after splitting by space
    ip = str.split()

    # Create the root of the tree
    root = Node(int(ip[0]))

    # Push the root to the queue
    queue = deque()
    queue.append(root)

    # Starting from the second element
    i = 1
    while queue and i < len(ip):
        # Get and remove the front of the queue
        currNode = queue.popleft()

        # Get the current node's value from the string
        currVal = ip[i]

        # If the left child is not null
        if currVal != "N":
            # Create the left child for the current node
            currNode.left = Node(int(currVal))

            # Push it to the queue
            queue.append(currNode.left)

        # For the right child
        i += 1
        if i >= len(ip):
            break
        currVal = ip[i]

        # If the right child is not null
        if currVal != "N":
            # Create the right child for the current node
            currNode.right = Node(int(currVal))

            # Push it to the queue
            queue.append(currNode.right)

        i += 1

    return root

for _ in range(int(input())):
    s = input()
    root = buildTree(s)
    k, x, y = map(int, input().split())
    if root is None:
        continue
    
    if root.left is None and root.right is None:
        continue
    
    ob = Solution()
    print(ob.kthCommonAncestor(root, k, x, y))


# } Driver Code Ends