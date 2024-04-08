class Solution:
    def countStudents(self, st: List[int], sa: List[int]) -> int:
        st,sa=deque(st),deque(sa)
        served=0
        while st:
            if st[0]==sa[0]:
                st.popleft()
                sa.popleft()
                served=0
            else:
                st.rotate(-1)
                served+=1
                if served==len(st): break
        return len(st)