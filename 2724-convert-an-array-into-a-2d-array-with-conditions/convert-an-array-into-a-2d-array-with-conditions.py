class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        tarr=[]
        c=Counter(nums)
        it=c.keys()
        while any(v for v in c.values()):
            carr=[]
            for num in it:
                if c[num]>0: carr.append(num);c[num]-=1
            tarr.append(carr)
        return tarr