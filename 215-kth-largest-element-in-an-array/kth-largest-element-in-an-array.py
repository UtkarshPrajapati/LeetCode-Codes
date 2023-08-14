class Solution:
    def findKthLargest(self,a,k):
        return heapq.nlargest(k,a)[-1]