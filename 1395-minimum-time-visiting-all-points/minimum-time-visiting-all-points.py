class Solution:
    def minTimeToVisitAllPoints(self,l):
        return sum(max(abs(l[i+1][0]-l[i][0]),abs(l[i+1][1]-l[i][1])) for i in range(len(l)-1))