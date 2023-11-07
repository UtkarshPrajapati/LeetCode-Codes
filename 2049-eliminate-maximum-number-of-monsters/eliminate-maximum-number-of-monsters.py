import heapq
class Solution:
    def eliminateMaximum(self, dist, speed):
        time = [i/j for i,j in zip(dist,speed)]
        heapq.heapify(time)
        i=0
        while time:
            if time[0]<=i: return i
            heapq.heappop(time)
            i+=1
        return i