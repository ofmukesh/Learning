class Solution:
    def findMin(self, nums: List[int]) -> int:
        # if given arr rotated 0 times, so the first ele is the minimum 
        if nums[0]<nums[-1] or len(nums)==1:
            return nums[0];

        l=0
        r=len(nums)-1;
        while l <= r:
            mid=int((l+r)/2)
            if nums[mid]>nums[mid+1]:
                return nums[mid+1]
            elif nums[mid-1]>nums[mid]:
                return nums[mid]
            elif nums[l]<nums[mid]:
                l=mid
            else:
                r=mid-1
        return nums[l]
             
