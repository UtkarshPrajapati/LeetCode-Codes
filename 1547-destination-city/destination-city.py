class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        ca,cb=set(),set()
        for i in paths:
            ca.add(i[0])
            cb.add(i[1])
        for i in cb:
            if i not in ca: return i