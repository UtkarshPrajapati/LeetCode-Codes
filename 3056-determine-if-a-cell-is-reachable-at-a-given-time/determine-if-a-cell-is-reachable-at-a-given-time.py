class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        if sx==fx and sy==fy: return True if t!=1 else False
        d=max(abs(sx-fx),abs(sy-fy))
        return True if d<=t else False