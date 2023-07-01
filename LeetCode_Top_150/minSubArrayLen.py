class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        strt=0
        end=0
        min_l=len(nums)+1
        curr_sum=0
        
        while end<len(nums) and strt<len(nums):
            curr_sum+=nums[end] # adding curr ele to sum
            while curr_sum >= target and strt <= end: # shrinking current subarray from start if current sum is greater than target while current sum not less than target
                min_l = min(min_l, end - strt + 1)
                curr_sum-=nums[strt]
                strt +=1
            end+=1 # expanding current subarray

        return min_l if min_l!=len(nums)+1 else 0
