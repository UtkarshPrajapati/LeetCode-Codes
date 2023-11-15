class Solution:
    def maximumElementAfterDecrementingAndRearranging(self,arr):
        arr.sort()
        c=1
        for i in range(1,len(arr)):
            if arr[i]>c: c+=1
        return c