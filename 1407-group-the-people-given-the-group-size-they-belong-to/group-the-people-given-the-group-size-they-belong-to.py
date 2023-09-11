class Solution:
    def groupThePeople(self,g):
        dp={}
        for i in range(len(g)):
            dp[g[i]]=dp.get(g[i],[])+[i]
        a=[]
        for i in dp.keys():
            if i==len(dp[i]): a.append(dp[i])
            else:
                for j in range(len(dp[i])//i):
                    a.append(dp[i][j*i:j*i+i])
        return a