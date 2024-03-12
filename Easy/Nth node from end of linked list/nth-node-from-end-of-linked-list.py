#User function Template for python3
'''
	Your task is to return the data stored in
	the nth node from end of linked list.
	
	Function Arguments: head (reference to head of the list), n (pos of node from end)
	Return Type: Integer or -1 if no such node exits.

	{
		# Node Class
		class Node:
		    def __init__(self, data):   # data -> value stored in node
		        self.data = data
		        self.next = None
	}
'''
#Function to find the data of nth node from the end of a linked list

def getNthFromLast(head, n):
    # Initializing two pointers
    pointer1 = head
    pointer2 = head
    
    # Move pointer2 to the nth node from the beginning
    for _ in range(n):
        if pointer2 is None:
            return -1  # If the linked list is shorter than n
        pointer2 = pointer2.next
    
    # Move both pointers simultaneously until pointer2 reaches the end
    while pointer2 is not None:
        pointer1 = pointer1.next
        pointer2 = pointer2.next
    
    # At this point, pointer1 is at the nth node from the end
    if pointer1 is None:
        return -1  # If pointer1 is None, the linked list is shorter than n
    else:
        return pointer1.data\


#{ 
 # Driver Code Starts
#Initial Template for Python 3


import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())
    
# Node Class
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None

# Linked List Class
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # creates a new node with given value and appends it at the end of the linked list
    def append(self, new_value):
        new_node = Node(new_value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        self.tail.next = new_node
        self.tail = new_node

if __name__ == '__main__':
    t=int(input())
    for cases in range(t):
        n,nth_node = map(int, input().strip().split())
        a = LinkedList() # create a new linked list 'a'.
        nodes_a = list(map(int, input().strip().split()))
        for x in nodes_a:
            a.append(x)  # add to the end of the list
        print(getNthFromLast(a.head,nth_node))
# } Driver Code Ends