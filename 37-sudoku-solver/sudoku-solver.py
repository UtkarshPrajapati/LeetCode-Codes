class Solution:
    def solveSudoku(self,b):
        rows, cols, triples, visit = [set() for _ in range(9)], [set() for _ in range(9)], [set() for _ in range(9)], [(i, j) for i in range(9) for j in range(9) if b[i][j]=="."]
        for i,j in [(i,j) for i in range(9) for j in range(9) if b[i][j]!="."]:
            e=b[i][j]
            rows[i].add(e)
            cols[j].add(e)
            triples[(i//3)*3+j//3].add(e)
        def dfs():
            if not visit: return True
            i,j=visit[0]
            for num in "123456789":
                if num not in rows[i]|cols[j]|triples[(i//3)*3+j//3]:
                    visit.pop(0)
                    rows[i].add(num)
                    cols[j].add(num)
                    triples[(i//3)*3+j//3].add(num)
                    b[i][j]=num
                    if dfs(): return True
                    visit.insert(0,(i,j))
                    rows[i].remove(num)
                    cols[j].remove(num)
                    triples[(i//3)*3+j//3].remove(num)
                    b[i][j]="."
            return False
        dfs()