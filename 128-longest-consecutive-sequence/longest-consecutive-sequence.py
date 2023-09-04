class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s,m=set(nums),0
        for num in s:
            if num-1 not in s:
                i,cs=num,1
                while i+1 in s: i+=1;cs+=1
                m=max(m,cs)
        return m