class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        n=len(nums)
        ans=float('inf')
        left_arr = [1e7] * n
        right_arr = [1e8] * n

        left_arr[0] = nums[0]

        for i in range(1, n):
            left_arr[i] = min(left_arr[i - 1], nums[i])

        right_arr[n - 1] = nums[n - 1]
        for i in range(n - 2, -1, -1):
            right_arr[i] = min(right_arr[i + 1], nums[i])

        for i in range(1, n - 1):
            if left_arr[i - 1] < nums[i] and right_arr[i + 1] < nums[i]:
                ans = min(ans, left_arr[i - 1] + right_arr[i + 1] + nums[i])

        return ans if ans != float('inf') else -1
