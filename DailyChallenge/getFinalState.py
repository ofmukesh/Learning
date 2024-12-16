class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        for _ in range(k):
            idx=0
            mini=nums[0]

            for i,num in enumerate(nums):
                if num<mini:
                    mini=num
                    idx=i
            
            nums[idx]=nums[idx]*multiplier

        return nums
