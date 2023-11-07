import numpy as np
class Solution:
    def eliminateMaximum(self,dist,speed):
        time=np.sort(np.array(dist)/np.array(speed))
        ans=1
        for i,e in enumerate(time):
            if e<=i: return i
        return i+1