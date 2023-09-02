class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n=len(nums);s=n-k%n
        nums[:]=nums[s:]+nums[:s]