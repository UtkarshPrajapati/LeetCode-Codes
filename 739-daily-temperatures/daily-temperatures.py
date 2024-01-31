class Solution:
    def dailyTemperatures(self, T):
        ans,st=[0]*len(T),[]
        for i,v in enumerate(T):
            while st and st[-1][1]<v:
                index,_=st.pop()
                ans[index]=i-index
            st.append([i,v])      
        return ans