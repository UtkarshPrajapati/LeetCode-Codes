class MyStack:
    def __init__(self):
        self.q1=[]
        self.q2=[]
    def push(self, x: int) -> None:
        self.q1.append(x)
    def pop(self) -> int:
        while len(self.q1)>1:
            self.q2.append(self.q1.pop(0))
        a=self.q1.pop(0)
        self.q1,self.q2=self.q2,self.q1
        return a
    def top(self) -> int:
        return self.q1[-1]
    def empty(self) -> bool:
        print(self.q1)
        return len(self.q1)==0