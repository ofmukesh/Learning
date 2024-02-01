# slide window if curr sum is negative else add curr num to curr sum and find max sum of subarray
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxArrSum=nums[0]
        currSum=0

        for num in nums:
            if currSum<0:
                currSum=0
            currSum+=num
            maxArrSum=max(maxArrSum,currSum)
        
        return maxArrSum
