class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        max_val = max(arr)
        win, c = arr[0], 0
        for i in arr[1:]:
            if win < i: win, c = i, 1
            else: c += 1
            if c == k or win == max_val: return win
        return win