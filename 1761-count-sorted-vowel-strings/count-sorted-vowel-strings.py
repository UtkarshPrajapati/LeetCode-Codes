class Solution:
    def countVowelStrings(self, N: int) -> int:
        return int(math.factorial(N+4)/(math.factorial(4)*math.factorial(N)))