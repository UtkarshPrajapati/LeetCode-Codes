class Solution:
    def maxLength(self,arr):
        maxlen,unique=0,['']
        def isvalid(s): return len(s)==len(set(s))
        for word in arr:
            for j in unique:
                tmp=word+j
                if isvalid(tmp):
                    unique.append(tmp)
                    maxlen=max(maxlen,len(tmp))
        return maxlen