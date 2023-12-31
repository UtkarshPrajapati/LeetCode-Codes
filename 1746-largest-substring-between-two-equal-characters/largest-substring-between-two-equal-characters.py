class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        le,d=-1,{}
        for i,ch in enumerate(s):
            if ch not in d: d[ch]=i
            else: le=max(le,i-d.get(ch)-1)
        return le