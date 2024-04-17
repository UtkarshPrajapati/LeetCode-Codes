class Solution:
    def smallestFromLeaf(self, root):
        def dfs(node, path):
            if node:
                path = chr(97 + node.val) + path
                if not node.left and not node.right:
                    return path
                if node.left and node.right:
                    return min(dfs(node.left, path), dfs(node.right, path))
                elif node.left:
                    return dfs(node.left, path)
                else:
                    return dfs(node.right, path)
            return '~'

        return dfs(root, '')