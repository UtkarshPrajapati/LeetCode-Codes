class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points.sort()
        d=0
        for i in range(len(points)):
            d=max(d,points[i][0]-points[i-1][0])
        return d