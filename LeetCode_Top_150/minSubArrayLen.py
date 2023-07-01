class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        strt=0
        end=0
        min_l=len(nums)+1
        curr_sum=0
        
        while end<len(nums) and strt<len(nums):
            curr_sum+=nums[end]
            while curr_sum >= target and strt <= end:
                min_l = min(min_l, end - strt + 1)
                curr_sum-=nums[strt]
                strt +=1
            end+=1

        return min_l if min_l!=len(nums)+1 else 0
