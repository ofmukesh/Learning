class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        frq={}

        i=0
        while i<len(nums):
            if frq.get(nums[i]) and frq[nums[i]]>=2:
                del nums[i]
            else:
                frq[nums[i]]=1+frq.get(nums[i],0)
                i+=1
        
 
