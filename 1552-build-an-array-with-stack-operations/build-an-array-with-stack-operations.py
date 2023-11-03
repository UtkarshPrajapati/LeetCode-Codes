class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        s = []
        for i in range(1, n+1):
            if i in target:
                s.append("Push")
                target.remove(i)
            else: s.extend(["Push","Pop"])
            if not target: break
        return s