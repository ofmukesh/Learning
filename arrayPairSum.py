class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        ordrd_nums=sorted(nums)
        
        i=0
        ans=0
        while i<len(ordrd_nums):
            ans+=min(ordrd_nums[i],ordrd_nums[i+1])
            i+=2
        
        return ans
