class Solution:
    def largestRectangleArea(self,heights):
        heights.append(0)
        stack,max_area=[-1],0
        for i in range(len(heights)):
            while heights[i]<heights[stack[-1]]:
                max_area=max(max_area,heights[stack.pop()]*(i-stack[-1]-1))
            stack.append(i)
        return max_area