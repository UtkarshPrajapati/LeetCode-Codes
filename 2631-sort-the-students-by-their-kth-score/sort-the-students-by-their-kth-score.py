class Solution:
    def sortTheStudents(self, score: List[List[int]], k: int) -> List[List[int]]:
        n=len(score)
        a = [score[i][k] for i in range(n)]
        b = sorted(a, reverse=True)
        c = {i: b.index(a[i]) for i in range(n)}
        sorted_score = [None] * n
        for i in range(n):
            sorted_score[c[i]] = score[i]
        return sorted_score