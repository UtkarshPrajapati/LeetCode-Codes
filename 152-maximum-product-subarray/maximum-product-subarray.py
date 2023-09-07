class Solution:
    def maxProduct(self,arr):
        n,pre,suf,ans=len(arr),1,1,float('-inf')
        for i in range(n):
            if pre==0: pre=1
            if suf==0: suf=1
            pre,suf=pre*arr[i],suf*arr[n-i-1]
            ans=max([ans,pre,suf])
        return ans