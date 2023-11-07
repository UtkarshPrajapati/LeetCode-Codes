class Solution:
    def eliminateMaximum(self,dist,speed):
        time,ans=sorted([(i/j) for i,j in zip(dist,speed)]),1
        for i,e in enumerate(time):
            if e<=i: return i
        return i+1