class Solution(object):
    def countPalindromicSubsequence(self,s):
        d=defaultdict(list)
        for i,c in enumerate(s): d[c].append(i)
        ans,char=0,set(s)
        for el in d:
            if len(d[el])<2: continue
            ans+=len(char.intersection(s[d[el][0]+1:d[el][-1]]))
        return ans