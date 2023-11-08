class Solution:
    def isReachableAtTime(self,sx,sy,fx,fy,t):
        if sx==fx and sy==fy: return True if t!=1 else False
        return True if max(abs(sx-fx),abs(sy-fy))<=t else False