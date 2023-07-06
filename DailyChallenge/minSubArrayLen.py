class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        ans = float('inf') # minimum length of subarray
        left = 0 # left pointer
        current_sum = 0 # current sum of elements in subarray

        for right in range(len(nums)):
            current_sum += nums[right] # include current element in the sum

            # check if the sum exceeds or equals the target
            while current_sum >= target:
                current_sum -= nums[left] # subtract the leftmost element from the sum
                ans = min(ans, right - left + 1) # update the minimum length
                left += 1 # move the left pointer to the right

        # if no valid subarray is found, return 0
        if ans == float('inf'):
            return 0

        return ans
