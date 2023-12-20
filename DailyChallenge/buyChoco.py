class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        mini=min(prices)
        prices.pop(prices.index(mini))
        mini2=min(prices)

        if money<mini+mini2:
            return money 
        else:
            return money-(mini+mini2)
