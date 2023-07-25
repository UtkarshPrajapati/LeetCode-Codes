import numpy as np
class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        arr=np.array(arr)
        return np.where(arr==np.max(arr))[0][0]