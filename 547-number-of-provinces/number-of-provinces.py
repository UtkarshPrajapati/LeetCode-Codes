def dfs(node,visited,n,isConnected):
    visited[node]=True
    for neighbor in range(n):
        if isConnected[node][neighbor] and not visited[neighbor]: dfs(neighbor,visited,n,isConnected)
class Solution:
    def findCircleNum(self, isConnected):
        n=len(isConnected);p=0;visited=[False]*n
        for i in range(n):
            if not visited[i]: p+=1;dfs(i,visited,n,isConnected)
        return p