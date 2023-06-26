class Solution:
    def totalCost(self, costs, k, candidates):
        i,j,ans = 0,len(costs) - 1,0
        pq1,pq2 = [],[]
        while k > 0:
            while len(pq1) < candidates and i <= j:
                heapq.heappush(pq1, costs[i])
                i += 1
            while len(pq2) < candidates and i <= j:
                heapq.heappush(pq2, costs[j])
                j -= 1
            t1,t2 = pq1[0] if pq1 else float('inf'),pq2[0] if pq2 else float('inf')
            if t1 <= t2:
                ans += t1
                heapq.heappop(pq1)
            else:
                ans += t2
                heapq.heappop(pq2)
            k -= 1
        return ans