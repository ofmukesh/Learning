class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        start_rotate=k%len(nums)

        l=len(nums)-start_rotate
    
        for i in range(l):
            nums.append(nums.pop(0))
