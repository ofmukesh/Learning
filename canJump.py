class Solution:
    def canJump(self, nums: List[int]) -> bool:
        reach=0
        i=0
        while i<len(nums):
            if reach<i:
                return False
            reach=max(reach,i+nums[i])
            i+=1

        return True
