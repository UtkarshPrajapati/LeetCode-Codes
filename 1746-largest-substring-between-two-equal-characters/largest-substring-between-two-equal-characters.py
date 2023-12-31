class Solution:
    def maxLengthBetweenEqualCharacters(self,s):
        return max(s.rfind(ch)-s.find(ch)-1 for ch in set(s))