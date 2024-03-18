class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        n=len(points)
        if not points: return 0
        points.sort(key=lambda x:x[0])
        cnt=0
        end=points[0][1]
        for i in range(1,n):
            if points[i][0]<=end:
                cnt+=1
                end=min(end,points[i][1])
            else: end=points[i][1]
        return n-cnt