class Solution:
    def kWeakestRows(self,mat,k):
        heap=[(sum(row),i) for i,row in enumerate(mat)]
        heapq.heapify(heap)
        return [heapq.heappop(heap)[1] for _ in range(k)]