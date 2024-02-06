class Solution:
    def groupAnagrams(self, strs):
        d=defaultdict(list)
        for i in strs: d[''.join(sorted(i))].append(i)
        return list(d.values())