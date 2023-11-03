class Solution:
    def isValid(self,s):
        st,d=[],{"]":"[", "}":"{", ")":"("}
        for c in s:
            if c in ['[', '{', '(']: st.append(c)
            elif c in [']', '}', ')'] and st==[] or d[c]!=st.pop(): return False
        return st==[]