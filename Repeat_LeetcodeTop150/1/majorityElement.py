
############################# T.C-> O(n) ######################
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        candidate = 0
        
        for num in nums:
            if count == 0:
                candidate = num
            
            if num == candidate:
                count += 1
            else:
                count -= 1
        
        return candidate

'''
########################### Not optimized solution ####################
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count=1
        max_c=0
        ans=nums[0]
        nums=sorted(nums)

        for i in range(len(nums)-1):
            if nums[i]==nums[i+1]:
                count+=1
            else:
                count=1
            if max_c<count:
                max_c=count
                ans=nums[i]
        return ans
'''

'''
############################# T.C-> O(n log n) ######################
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums=sorted(nums)
        return nums[int(len(nums)/2)]
'''
