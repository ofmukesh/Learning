class Solution:
    def findValueOfPartition(self, nums: List[int]) -> int:
        nums=sorted(nums)
        
        mini=-1
        
        for i in range(len(nums)-1):
            dif=nums[i+1]-nums[i]
            if mini==-1 or dif<mini:
                mini=dif
        
        return mini
                
