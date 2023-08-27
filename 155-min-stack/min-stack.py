class MinStack:
    def __init__(self):
        self.s=[]
    def push(self, val: int) -> None:
        self.s+=[val]
    def pop(self) -> None:
        n=len(self.s)
        self.s=self.s[:n-1]
    def top(self) -> int:
        return self.s[-1]
    def getMin(self) -> int:
        return min(self.s)