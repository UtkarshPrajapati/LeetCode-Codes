class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        a=min(prices)
        prices.remove(a)
        b=min(prices)
        return money-a-b if a+b<=money else money