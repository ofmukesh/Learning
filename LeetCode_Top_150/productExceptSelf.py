#2 optimized 
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        o=[1]*(len(nums));

        p=1;
        for i in range(len(nums)):
            o[i]=p;
            p*=nums[i];
            
        p=1;
        for i in range(len(nums)-1,-1,-1):
            o[i]*=p;
            p*=nums[i];

        return o;
#1 
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left=[1 for _ in nums]
        right=[1 for _ in nums]

        p=1
        for i in range(len(nums)):
            left[i]=p
            p*=nums[i]
        
        p=1
        for i in range(len(nums)-1,-1,-1):
            right[i]=p
            p*=nums[i]

        for i in range(len(nums)):
            nums[i]=left[i]*right[i]

        return nums
