class NestedIterator:
    def __init__(self,l):
        self.s = l[::-1]
    def next(self):
        return self.s.pop().getInteger()
    def hasNext(self):
        while self.s:
            top=self.s[-1]
            if top.isInteger(): return True
            self.s=self.s[:-1]+top.getList()[::-1]
        return False