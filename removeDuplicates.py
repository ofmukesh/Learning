class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        temp={}
        i=0
        while i < len(nums):
            num=nums[i]
            if temp.get(num)!=None:
                del nums[i]
            else:
                temp[num]=1
                i+=1
