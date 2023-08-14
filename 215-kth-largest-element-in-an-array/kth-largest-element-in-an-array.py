class Solution:
    def findKthLargest(self,a,k):
        def partition(l,r):
            p=a[r]
            i=l
            for j in range(l,r):
                if a[j]>p:
                    a[i],a[j]=a[j],a[i]
                    i+=1
            a[i],a[r]=a[r],a[i]
            return i
        l,r,k=0,len(a)-1,k-1
        while l<=r:
            pi=partition(l,r)
            if pi==k: return a[k]
            elif pi<k: l=pi+1
            else: r=pi-1