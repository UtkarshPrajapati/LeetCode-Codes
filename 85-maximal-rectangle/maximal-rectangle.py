class Solution:
    def maximalRectangle(self, matrix):
        if not matrix or not matrix[0]: return 0
        n = len(matrix[0])
        height,ans=[0]*(n+1),0
        for row in matrix:
            stack = [-1]
            for i in range(n):
                height[i] = height[i] + 1 if row[i] == '1' else 0
            for i in range(n + 1):
                while height[i] < height[stack[-1]]:
                    h = height[stack.pop()]
                    w = i if stack[-1] == -1 else i - stack[-1] - 1
                    ans = max(ans, h * w)
                stack.append(i)
        return ans