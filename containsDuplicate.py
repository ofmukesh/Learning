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

    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums)!=len(set(nums))
