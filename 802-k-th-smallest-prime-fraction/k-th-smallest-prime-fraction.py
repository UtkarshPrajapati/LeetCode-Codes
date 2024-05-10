class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        frac=[(arr[i]/arr[j],i,j) for i in range(len(arr)) for j in range(i+1,len(arr))]
        heapq.heapify(frac)
        for _ in range(k): sfrac=heapq.heappop(frac)
        return [arr[sfrac[1]],arr[sfrac[2]]]