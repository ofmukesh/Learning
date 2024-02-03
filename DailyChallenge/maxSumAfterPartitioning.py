class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        # Length of the input array
        n = len(arr)
        
        # Dynamic programming table to store maximum sum at each position
        dp = [0]*(n+1)
        
        # Iterate through the array elements
        for i in range(n):
            curMax = curSum = 0
            
            # Iterate over the last k elements or until the beginning of the array
            for j in range(i, max(-1, i-k), -1):
                # Update the maximum value in the current partition
                if curMax < arr[j]:
                    curMax = arr[j]
                
                # Calculate the current sum considering the maximum value in the partition
                cur = curMax * (i - j + 1) + dp[j]
                
                # Update the current sum if the new one is greater
                if curSum < cur:
                    curSum = cur
            
            # Update the dynamic programming table with the maximum sum at the current position
            dp[i+1] = curSum

        
        return dp[-1]
