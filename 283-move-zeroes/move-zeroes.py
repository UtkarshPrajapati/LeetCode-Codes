class Solution:
    def moveZeroes(self,a):
        b,n=[],len(a)
        for i in range(n):
            if a[i]!=0: b.append(a[i])
        nums=b+[0]*(n-len(b))
        a[:]=nums[:]