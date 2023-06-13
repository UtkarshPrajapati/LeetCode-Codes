class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        nrow,c=defaultdict(int),0
        for row in grid: nrow[tuple(row)]+=1
        for column in zip(*grid): c+=nrow[column]  
        return c