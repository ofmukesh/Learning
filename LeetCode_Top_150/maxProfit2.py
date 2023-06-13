class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit=0
        min_price=prices[0]

        for curr_price in prices:
            if curr_price > min_price:
                profit+=curr_price-min_price
            min_price=curr_price
        
        return profit
