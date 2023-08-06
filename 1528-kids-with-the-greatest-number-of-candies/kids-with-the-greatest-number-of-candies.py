class Solution:
    def kidsWithCandies(self, c: List[int], ec: int) -> List[bool]:
        m=max(c)
        return [i+ec>=m for i in c]