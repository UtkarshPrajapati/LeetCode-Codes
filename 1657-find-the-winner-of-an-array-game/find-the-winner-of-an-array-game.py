class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        win, c = arr[0], 0
        for i in arr[1:]:
            if win > i: c += 1
            else: win, c = i, 1
            if c == k: return win
        return win