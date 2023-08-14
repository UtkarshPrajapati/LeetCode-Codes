class Solution:
    def findKthLargest(self,a,k):
        def partition(l,r):
            pi=randrange(l,r+1)
            a[pi],a[r]=a[r],a[pi]
            p,i=a[r],l
            for j in range(l,r):
                if a[j]>p: a[i],a[j]=a[j],a[i];i+=1
            a[i],a[r]=a[r],a[i]
            return i
        l,r,k=0,len(a)-1,k-1
        while l<=r:
            pi=partition(l,r)
            if pi==k: return a[k]
            l,r=(pi+1,r) if pi<k else (l,pi-1)