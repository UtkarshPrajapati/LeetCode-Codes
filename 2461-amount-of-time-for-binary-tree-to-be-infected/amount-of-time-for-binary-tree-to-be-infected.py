class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        def addParent(node, parent=None):
            if node:
                node.parent = parent
                if node.val == start: self.startNode = node
                addParent(node.left, node)
                addParent(node.right, node)
        def maxDepth(node,seen):
            if node and node not in seen:
                seen.add(node)
                return 1+max(maxDepth(node.left,seen),maxDepth(node.right,seen),maxDepth(node.parent,seen))
            return 0
        addParent(root)
        return maxDepth(self.startNode,set()) - 1