class MinStack:
    def __init__(self):
        self.s=[]
        self.ms=[]
    def push(self, val: int) -> None:
        self.s+=[val]
        self.ms+=[min(val,self.ms[-1]) if self.ms else val]
    def pop(self) -> None:
        n,nn=len(self.s),len(self.ms)
        self.s=self.s[:n-1]
        self.ms=self.ms[:nn-1]
    def top(self) -> int:
        return self.s[-1]
    def getMin(self) -> int:
        return self.ms[-1]