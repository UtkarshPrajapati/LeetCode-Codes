class Solution:
    def frequencySort(self,s):
        st,c="",Counter(s)
        for i in sorted(zip(c.keys(),c.values()),key=lambda x:x[1],reverse=True):
            st+=i[0]*i[1]
        return st