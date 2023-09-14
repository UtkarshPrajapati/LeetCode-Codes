class Solution:
    def findKthPositive(self,arr,k):
        l,r=0,len(arr)
        while l<r:
            m=(l+r)//2
            if arr[m]-m-1<k: l=m+1
            else: r=m
        return l+k