class StockSpanner:
    def __init__(self):
        self.l = []
    def next(self, price: int) -> int:
        span = 1
        while self.l and self.l[-1][0]<=price:
            span += self.l.pop()[1]
        self.l.append((price,span))
        return span