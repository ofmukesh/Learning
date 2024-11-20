class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        data={}

        for num in nums:
            if data.get(num):
                return True
            data[num]=True
        
        return False
