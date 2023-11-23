class Solution:
    def checkArithmeticSubarrays(self,nums,l,r):
        def check(arr):
            arr.sort()
            return len(set(j-i for i,j in zip(arr,arr[1:])))==1
        return [check(nums[i:j+1]) for i, j in zip(l, r)]