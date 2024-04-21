class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, dest: int) -> bool:
        d=defaultdict(list)
        for i in edges:
            d[i[0]].append(i[1])
            d[i[1]].append(i[0])
        rem=set(range(n))
        st=[source]
        while st:
            curr=st.pop()
            if curr==dest: return True
            if curr in rem: rem.remove(curr)
            st.extend(nei for nei in d[curr] if nei in rem)
        return False