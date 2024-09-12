class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        lpa=[1]
        for num in nums:
            lpa.append(lpa[-1]*num)
        lpa.pop()
        
        rpt=1
        for i in range(len(nums)-1,-1,-1):
            tmp=nums[i]
            nums[i]=lpa[i]*rpt
            rpt=rpt*tmp
        
        return nums
