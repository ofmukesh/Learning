class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr_sum=0
        ans=nums[0]

        for n in nums:
            curr_sum+=n
            ans=max(ans,curr_sum)
            if curr_sum<0:
                curr_sum=0

        return ans
