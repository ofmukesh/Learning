class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l=0
        h=len(nums)-1
        if nums[0]==target:
            return 0
        elif target == nums[h]:
            return h
        elif target>nums[h] or target < nums[0]:
            return -1
        else:
            while l!=h:
                mid=int((l+h)/2)
                num=nums[mid]
                if num==target:
                    return mid
                elif num<target:
                    l=mid
                elif num>target:
                    h=mid
                if l+1==h:
                    return -1
