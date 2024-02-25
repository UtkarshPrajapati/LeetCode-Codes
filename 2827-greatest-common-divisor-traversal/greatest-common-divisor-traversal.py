class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        if len(nums)==1: return True
        n, f, num, have = len(nums), list(range(len(nums))), [1]*len(nums), {}
        def getf(x: int) -> int:
            f[x] = x if f[x] == x else getf(f[x])
            return f[x]
        def merge(x: int, y: int):
            x, y = getf(x), getf(y)
            if x != y:
                if num[x] < num[y]: x, y = y, x
                f[y], num[x] = x, num[x] + num[y]
        for i, x in enumerate(nums):
            if x == 1: return False
            for d in range(2, int(x**0.5)+1):
                if x % d == 0:
                    merge(i, have.setdefault(d, i))
                    while x % d == 0: x //= d
            if x > 1: merge(i, have.setdefault(x, i))
        return num[getf(0)] == n