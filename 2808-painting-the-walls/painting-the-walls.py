class Solution:
    def paintWalls(self,cost,time):
        postfix_times=time.copy()
        for i in range(len(postfix_times)-2,-1,-1):
            postfix_times[i]+=postfix_times[i+1]
        visited = {}
        def dp(index,t):
            if index==len(cost): return 0 if t>=0 else float("inf")
            if t>=len(cost)-index: return 0
            if t+postfix_times[index] < 0: return float("inf")
            if (index,t) in visited: return visited[(index,t)]
            visited[(index, t)] = min(dp(index+1,t-1),cost[index]+dp(index+1,t+time[index]))
            return visited[(index,t)]
        return dp(0,0)