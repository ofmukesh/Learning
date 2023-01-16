class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        t=nums[0]-nums[len(nums)-1];
        for i in range(len(nums)-1):
            if nums[i]>nums[i+1] and t<0:
                return False;
            elif nums[i]<nums[i+1] and t>0:
                return False;
            elif t==0 and nums[i]!=nums[i+1]:
                return False;
        return True
                
