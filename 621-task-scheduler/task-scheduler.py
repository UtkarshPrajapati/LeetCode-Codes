class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        le=len(tasks)
        if n==0: return le
        d=list(Counter(tasks).values())
        m=max(d)
        return max(len(tasks),(m-1)*(n+1)+d.count(m))