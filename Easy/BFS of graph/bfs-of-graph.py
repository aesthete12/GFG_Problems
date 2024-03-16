#User function Template for python3

from typing import List
from queue import Queue
class Solution:
    # Function to return Breadth First Traversal of given graph.
    def bfsOfGraph(self, V: int, adj: List[List[int]]) -> List[int]:
        visited = [False] * V
        result = []

        # Create a queue for BFS
        queue = Queue()
        queue.put(0)
        visited[0] = True

        while not queue.empty():
            # Dequeue a vertex from queue
            vertex = queue.get()
            result.append(vertex)

            # Get all adjacent vertices of the dequeued vertex vertex.
            # If an adjacent has not been visited, then mark it visited
            # and enqueue it.
            for adj_vertex in adj[vertex]:
                if not visited[adj_vertex]:
                    queue.put(adj_vertex)
                    visited[adj_vertex] = True

        return result

#{ 
 # Driver Code Starts


if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		V, E = map(int, input().split())
		adj = [[] for i in range(V)]
		for _ in range(E):
			u, v = map(int, input().split())
			adj[u].append(v)
		ob = Solution()
		ans = ob.bfsOfGraph(V, adj)
		for i in range(len(ans)):
		    print(ans[i], end = " ")
		print()
        

# } Driver Code Ends