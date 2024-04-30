class Solution:
    def wonderfulSubstrings(self,word):
        count,ans,mask=[0]*1024,0,0
        count[0]=1
        for c in word:
            mask^=1<<(ord(c)-97)
            ans+=count[mask]
            for i in range(10):
                ans+=count[mask^(1<<i)]
            count[mask]+=1
        return ans