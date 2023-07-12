class Solution:
    def isSafe(self, s, graph, visited, checkCycle):
        if visited[s] == 1: return True
        elif visited[s] == -1: return False
        visited[s] = -1
        for it in graph[s]:
            if not self.isSafe(it, graph, visited, checkCycle): return False
        visited[s] = 1
        return True
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        v = len(graph)
        visited = [0] * v
        checkCycle = []
        for i in range(v):
            if self.isSafe(i, graph, visited, checkCycle): checkCycle.append(i)
        return checkCycle