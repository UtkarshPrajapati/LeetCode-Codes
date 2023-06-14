class Solution:
    def getMinimumDifference(self, root):
        stack,curr = [],root
        prev_val,md=None,float('inf')
        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            if prev_val is not None: md=min(md,abs(curr.val-prev_val))
            prev_val = curr.val
            curr = curr.right
        return md