class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i=0
        while i < len(nums):
            if val==nums[i]:
                del nums[i]
            else:
                i+=1
