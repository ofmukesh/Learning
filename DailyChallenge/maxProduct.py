# find 2 maximum element of the array and this your answer 
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        first_max_idx=0
        first_max=nums[first_max_idx]

        for idx,num in enumerate(nums):
            if num>first_max:
                first_max=num
                first_max_idx=idx
                
        sec_max=0
        for idx,num in enumerate(nums):
            if idx!=first_max_idx and num>sec_max:
                sec_max=num
        
    
        return (first_max-1)*(sec_max-1)
