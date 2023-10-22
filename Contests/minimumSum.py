class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        ans=float('inf')
        
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                for k in range(j+1,len(nums)):
                    val1=nums[i]
                    val2=nums[j]
                    val3=nums[k]
                    if val1<val2>val3:
                        ans=min(ans,val1+val2+val3)
        
        if ans == float('inf'):
            return -1
        else:
            return ans
                    
