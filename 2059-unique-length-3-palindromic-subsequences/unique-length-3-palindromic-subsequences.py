class Solution(object):
    def countPalindromicSubsequence(self, s):
        charDict = defaultdict(list)
        for i, char in enumerate(s):
            if char not in charDict: charDict[char] = [i, i]
            else: charDict[char][1] = i
        ans = 0
        uniqueChars = set(s)
        for char in charDict:
            if charDict[char][1] - charDict[char][0] <= 1: continue
            ans += len(uniqueChars.intersection(s[charDict[char][0]+1 : charDict[char][1]]))
        return ans