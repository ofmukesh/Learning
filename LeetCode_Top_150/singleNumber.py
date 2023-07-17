class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        c=nums[0]
        for num in nums[1:]:
            c^=num

        return c
