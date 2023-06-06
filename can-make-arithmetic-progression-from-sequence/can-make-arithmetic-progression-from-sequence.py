class Solution:
    def canMakeArithmeticProgression(self,arr):
        if len(arr)==2: return True
        arr.sort()
        return 1==len({arr[i+1]-arr[i] for i in range(len(arr)-1)})