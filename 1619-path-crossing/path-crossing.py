class Solution:
    def isPathCrossing(self, path: str) -> bool:
        x, y, vis = 0, 0, {(0, 0)}
        for d in path:
            x += 1 if d == 'E' else (-1 if d == 'W' else 0)
            y += 1 if d == 'N' else (-1 if d == 'S' else 0)
            if (x, y) in vis: return True
            vis.add((x, y))
        return False