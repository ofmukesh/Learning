class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        temp={}
        for i in range(len(nums)):
            num=nums[i]
            if num in temp.keys():
                return True
            else:
                temp[num]=1
        return False

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            if nums[i] in nums[i+1:len(nums)]:
                return True
        return False
