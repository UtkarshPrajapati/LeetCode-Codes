class Solution:
    def find132pattern(self,nums):
        st,m=[],nums[0]
        for n in nums[1:]:
            while st and n>=st[-1][0]: st.pop()
            if st and n>st[-1][1]: return True
            st.append([n,m])
            m=min(m,n)
        return False