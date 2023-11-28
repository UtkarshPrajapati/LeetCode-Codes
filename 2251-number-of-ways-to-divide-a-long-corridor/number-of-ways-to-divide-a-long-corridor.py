class Solution:
    def numberOfWays(self,corridor):
        x,y,z=1,0,0
        for c in corridor:
            if c=='S': x,y,z=0,x+z,y
            else: x+=z
        return z%1000000007