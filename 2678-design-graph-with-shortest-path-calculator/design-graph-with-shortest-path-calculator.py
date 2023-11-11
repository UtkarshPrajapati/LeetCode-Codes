from collections import defaultdict
import heapq

class Graph:
    def __init__(self, n, edges):
        self.n = n
        self.adj = defaultdict(list)
        for a, b, c in edges: self.addEdge([a, b, c])
    def addEdge(self, edge):
        a, b, c = edge
        self.adj[a].append((b, c))
    def shortestPath(self, node1, node2):
        dist = [float("inf")] * self.n
        dist[node1] = 0
        pq = [(0, node1)]
        visited = set()
        while pq:
            dis, node = heapq.heappop(pq)
            if node in visited: continue
            visited.add(node)
            for adjnode, weight in self.adj[node]:
                newdist = dis + weight
                if newdist < dist[adjnode]:
                    dist[adjnode] = newdist
                    heapq.heappush(pq, (newdist, adjnode))
        return dist[node2] if dist[node2] != float("inf") else -1