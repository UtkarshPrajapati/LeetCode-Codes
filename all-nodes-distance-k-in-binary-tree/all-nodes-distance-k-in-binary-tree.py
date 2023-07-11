class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        def buildgraph(node,parent,graph):
            if not node: return
            if node not in graph: graph[node]=[]
            if parent: graph[parent].append(node);graph[node].append(parent)
            buildgraph(node.left, node, graph)
            buildgraph(node.right, node, graph)
        graph={}
        buildgraph(root,None,graph)
        q=[(target,0)]
        visited={target}
        res=[]
        while q:
            node,dis=q.pop(0)
            if dis==k: res.append(node.val)
            elif dis>k: break
            for neighbor in graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    q.append((neighbor, dis+1))
        return res