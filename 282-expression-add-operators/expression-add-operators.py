class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        if not num: return []
        ans, n = [], len(num)
        def dfs(i=0, tmp='', curr=0, last=0):
            if i == n and curr == target: ans.append(tmp); return
            for j in range(i+1, n+1):
                if j-i>1 and num[i] == '0': break
                now = int(num[i:j])
                if i == 0: dfs(j, str(now), now, now)
                else:
                    dfs(j, tmp+'+'+str(now), curr+now, now)
                    dfs(j, tmp+'-'+str(now), curr-now, -now)
                    dfs(j, tmp+'*'+str(now), curr-last+last*now, last*now)
        dfs()
        return ans