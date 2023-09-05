class Solution:
    def frequencySort(self, s: str) -> str:
        st,c="",Counter(s)
        for i in sorted([[i,j] for i,j in zip(c.keys(),c.values())],key=lambda x:x[1],reverse=True):
            st+=i[0]*i[1]
        return st