class Solution:
        def peakIndexInMountainArray(self,a):
            l,r=0,len(a)-1 
            while l<=r:
                m=(l+r)//2
                if a[m-1]<a[m]>a[m+1]: return m
                if a[m+1]>a[m]: l=m+1
                else: r=m