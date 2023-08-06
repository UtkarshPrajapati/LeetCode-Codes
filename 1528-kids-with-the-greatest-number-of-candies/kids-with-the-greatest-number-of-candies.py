class Solution:
    def kidsWithCandies(self, c: List[int], ec: int) -> List[bool]:
        m=max(c)
        return [True if i+ec>=m else False for i in c]