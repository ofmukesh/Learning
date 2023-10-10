class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        totalMaxProfit = 0  # Initialize the total maximum profit as 0.
        lastDayPrice = prices[0]  # Initialize the last day's price as the first price in the list.

        # Iterate through the list of prices.
        for curr_price in prices:
            if curr_price > lastDayPrice:
                # If the current price is higher than the last day's price, add the profit to the total profit.
                totalMaxProfit += curr_price - lastDayPrice
            lastDayPrice = curr_price  # Update the last day's price.

        # At the end of the loop, totalMaxProfit contains the maximum profit that can be obtained.
        return totalMaxProfit

# Time Complexity: O(n), where 'n' is the length of the 'prices' list. The algorithm makes a single pass through the list.
# Space Complexity: O(1) - The function uses a constant amount of extra space for variables regardless of the input size.
