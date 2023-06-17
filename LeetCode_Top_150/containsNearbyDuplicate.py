class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hashmap={}
        for i in range(len(nums)):
            
            if hashmap.get(nums[i])!=None:
                j=hashmap[nums[i]]
                if abs(i-j)<=k:
                    return True
            hashmap[nums[i]]=i
            
        return False
