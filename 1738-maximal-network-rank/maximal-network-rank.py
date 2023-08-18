class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        d = [sum([1 for u, v in roads if u == i or v == i]) for i in range(n)]
        s_d = sorted(set(d), reverse=True)
        m_d = s_d[0]
        s_m_d = s_d[1] if len(s_d) > 1 else 0
        m_c = d.count(m_d)
        s_m_c = d.count(s_m_d)
        if m_c > 1:
            dc = sum(1 for u, v in roads if d[u] == m_d and d[v] == m_d)
            pc = m_c * (m_c - 1) // 2
            return 2 * m_d - 1 if pc == dc else 2 * m_d
        dc_s = sum(1 for u, v in roads if (d[u], d[v]) in [(m_d, s_m_d), (s_m_d, m_d)])
        return m_d + s_m_d - 1 if s_m_c == dc_s else m_d + s_m_d