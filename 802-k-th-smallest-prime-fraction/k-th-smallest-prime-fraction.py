class Solution:
    def kthSmallestPrimeFraction(self,arr,k):
        sfrac=heapq.nsmallest(k,((arr[i]/arr[j],i,j) for i in range(len(arr)) for j in range(i+1,len(arr))))[-1]
        return [arr[sfrac[1]],arr[sfrac[2]]]