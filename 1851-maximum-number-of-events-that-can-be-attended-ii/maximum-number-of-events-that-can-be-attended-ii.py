class Solution:
    def maxValue(self, events, k):
        events.sort()
        @cache
        def f(i,k):
            
            return 0 if i>=len(events) or k<=0 else max(events[i][2]+f(bisect.bisect(events,[events[i][1]+1]),k-1),f(i+1,k))
        return f(0,k)