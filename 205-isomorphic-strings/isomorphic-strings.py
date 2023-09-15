class Solution:
    def isIsomorphic(self,s,t):
        print(set(zip(s,t)))
        return len(set(s))==len(set(t))==len(set(zip(s,t)))