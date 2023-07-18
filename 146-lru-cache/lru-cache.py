class LRUCache:
    class N:
        def __init__(s, k, v):
            s.k, s.v, s.p, s.n = k, v, None, None
    def __init__(s, c: int):
        s.c, s.m = c, {}
        s.h = s.t = s.N(-1, -1)
        s.h.n = s.t
        s.t.p = s.h
    def aN(s, n):
        t = s.h.n
        n.n, n.p = t, s.h
        s.h.n = t.p = n
    def dN(s, n):
        n.p.n = n.n
        n.n.p = n.p
    def get(s, k: int) -> int:
        if (rN := s.m.get(k)):
            a = rN.v
            del s.m[k]
            s.dN(rN)
            s.aN(rN)
            s.m[k] = s.h.n
            return a
        return -1
    def put(s, k: int, v: int) -> None:
        if k in s.m:
            c = s.m[k]
            del s.m[k]
            s.dN(c)
        if len(s.m) == s.c:
            del s.m[s.t.p.k]
            s.dN(s.t.p)
        s.aN(s.N(k, v))
        s.m[k] = s.h.n