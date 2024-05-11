class Solution:
    def mincostToHireWorkers(self, quality, wage, K):
        workers = sorted([w/q,q] for w,q in zip(wage,quality))
        heap=[]
        qsum=res=0
        for r,q in workers:
            heapq.heappush(heap,-q)
            qsum+=q
            if len(heap)>K: qsum+=heapq.heappop(heap)
            if len(heap)==K: res=min(res,qsum*r) if res else qsum*r
        return res