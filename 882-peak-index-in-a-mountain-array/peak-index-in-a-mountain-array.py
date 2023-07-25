class Solution:
    def peakIndexInMountainArray(self,a):
        l,r=0,len(a)-1
        while l<=r:
            if a[(m:=(l+r)//2)-1]<a[m]>a[m+1]: return m
            l,r=(m+1,r) if a[m+1]>a[m] else (l,m)