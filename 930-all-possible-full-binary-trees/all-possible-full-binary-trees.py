class Solution:
    def allPossibleFBT(self,n):
            dp={0:[],1:[TreeNode()]}
            for i in range(0,n,2): dp[i]=[]
            @cache
            def backtrack(n):
                if n in dp: return dp[n]
                res=[]
                for l in range(n):
                    lt,rt=backtrack(l),backtrack(n-l-1)
                    for t1 in lt:
                        for t2 in rt: res.append(TreeNode(0,t1,t2))
                dp[n]=res
                return res
            return backtrack(n)