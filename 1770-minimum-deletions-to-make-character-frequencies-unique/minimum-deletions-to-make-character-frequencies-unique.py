class Solution:
    def minDeletions(self, s):
        a,cnt=sorted(list(Counter(s).values()),reverse=True),0
        for i in range(len(a)-1):
            while a[i]<=a[i+1] and a[i+1]>0: a[i+1]-=1;cnt+=1
        return cnt