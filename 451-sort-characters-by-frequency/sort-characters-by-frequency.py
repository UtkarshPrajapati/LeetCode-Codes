class Solution:
    def frequencySort(self,s):
        return "".join(i[0]*i[1] for i in sorted(Counter(s).items(),key=lambda x:x[1],reverse=True))