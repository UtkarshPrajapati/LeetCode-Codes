class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        tarr=[]
        c=Counter(nums)
        while any(v for v in c.values()):
            carr=[]
            for num,cnt in c.items():
                if cnt>0: carr.append(num);c[num]-=1
            tarr.append(carr)
        return tarr