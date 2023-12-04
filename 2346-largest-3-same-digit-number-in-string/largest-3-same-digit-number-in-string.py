class Solution:
    def largestGoodInteger(self,n):
        m=""
        for i in range(len(n)-2):
            if n[i]==n[i+1]==n[i+2]: m=max(m,n[i:i+3])
        return m