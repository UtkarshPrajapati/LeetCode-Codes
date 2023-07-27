class Solution:
    def sumOfMultiples(self, n: int) -> int:
        return sum(i for i in range(n+1) if any(i%j==0 for j in [3,5,7]))