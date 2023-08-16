class Solution:
    def maxSlidingWindow(self,nums,k):
        n = len(nums)
        if k == 1: return nums
        deq = deque()
        for i in range(k):
            while deq and nums[i] > nums[deq[-1]]: deq.pop()
            deq.append(i)
        res = [nums[deq[0]]]
        for i in range(k, n):
            if deq and deq[0] == i - k: deq.popleft()
            while deq and nums[i] > nums[deq[-1]]: deq.pop()
            deq.append(i)
            res.append(nums[deq[0]])
        return res