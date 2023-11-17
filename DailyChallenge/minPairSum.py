class Solution(object):
    def minPairSum(self, nums):
        nums.sort()  # Sort the array
        left, right = 0, len(nums) - 1
        max_pair_sum = float('-inf')

        while left < right:
            pair_sum = nums[left] + nums[right]
            max_pair_sum = max(max_pair_sum, pair_sum)
            left += 1
            right -= 1

        return max_pair_sum
