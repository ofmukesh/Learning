########################### Not optimized solution ####################
# class Solution:
#     def majorityElement(self, nums: List[int]) -> int:
#         count=1
#         max_c=0
#         ans=nums[0]
#         nums=sorted(nums)

#         for i in range(len(nums)-1):
#             if nums[i]==nums[i+1]:
#                 count+=1
#             else:
#                 count=1
#             if max_c<count:
#                 max_c=count
#                 ans=nums[i]
        
#         return ans

############################# optimized solution ######################
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums=sorted(nums)
        return nums[int(len(nums)/2)]
