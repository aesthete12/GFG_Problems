#User function Template for python3

'''
class Node:
	def __init__(self, data):
		self.data = data
		self.next = None
		self.prev = None
'''

class Solution():
    def sortDoubly(self,head):
        if not head or not head.next:
            return head

        mid = self.findMiddle(head)
        mid_next = mid.next

        mid.next = None
        mid_next.prev = None

        left_sorted = self.sortDoubly(head)
        right_sorted = self.sortDoubly(mid_next)

        sorted_list = self.merge(left_sorted, right_sorted)

        return sorted_list

    def findMiddle(self, head):
        if not head:
            return head

        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def merge(self, left, right):
        dummy = Node(None)  
        current = dummy

        while left and right:
            if left.data <= right.data:
                current.next = left
                left.prev = current
                left = left.next
            else:
                current.next = right
                right.prev = current
                right = right.next
            current = current.next

        if left:
            current.next = left
            left.prev = current
        if right:
            current.next = right
            right.prev = current

        merged_head = dummy.next
        if merged_head:
            merged_head.prev = None

        return merged_head


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import sys

sys.setrecursionlimit(1000000)


class Node:

    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        new_node.prev = self.tail
        self.tail.next = new_node
        self.tail = new_node

    def printList(self, node):
        while (node.next is not None):
            node = node.next
        while node.prev is not None:
            node = node.prev
        while (node is not None):
            print(node.data, end=" ")
            node = node.next
        print()


def printList(node):
    temp = node

    while (node is not None):
        print(node.data, end=" ")
        temp = node
        node = node.next
    print()
    while (temp):
        print(temp.data, end=" ")
        temp = temp.prev


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        llist = DoublyLinkedList()
        for e in arr:
            llist.append(e)
        ob = Solution()
        llist.head = ob.sortDoubly(llist.head)
        printList(llist.head)
        print()

# } Driver Code Ends