class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0  # Initialize the maximum profit as 0.
        minPrice = prices[0]  # Initialize the minimum price as the first price in the list.

        # Iterate through the list of prices, starting from the second price.
        for currPrice in prices[1:]:
            maxProfit = max(maxProfit, currPrice - minPrice)  # Update maxProfit if a higher profit is found.
            minPrice = min(minPrice, currPrice)  # Update minPrice if a lower price is encountered.

        # At the end of the loop, maxProfit contains the maximum profit that can be obtained.
        return maxProfit

# Time Complexity: O(n), where 'n' is the length of the 'prices' list. The algorithm makes a single pass through the list.
# Space Complexity: O(1) - The function uses a constant amount of extra space for variables regardless of the input size.
