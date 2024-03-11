class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        d=defaultdict(list)
        for i,ch in enumerate(nums):
            if ch not in d: d[ch].append(i)
            elif i-d[ch][-1]<=k: return True
            d[ch].append(i)
        return False