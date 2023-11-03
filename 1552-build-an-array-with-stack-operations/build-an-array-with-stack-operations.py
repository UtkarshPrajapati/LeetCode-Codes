class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        ind=0
        s=[]
        for i in range(1,n+1):
            if ind<len(target):
                if target[ind]==i: s.append("Push");ind+=1
                else: s.extend(["Push","Pop"])
            else: break
        return s