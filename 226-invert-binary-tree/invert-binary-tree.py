class Solution:
    def invertTree(self,root):
        if root is None: return None
        queue=deque([root])
        while queue:
            node=queue.popleft()
            node.left,node.right=node.right,node.left
            if node.left: queue.append(node.left)
            if node.right: queue.append(node.right)
        return root