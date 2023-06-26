class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target<nums[0]:
            return 0
        elif target>nums[-1]:
            return len(nums)
        else:
            l=0
            r=len(nums)-1
            while l<r:
                mid=int((l+r)/2)
                if target==nums[mid]:
                    return mid 
                elif nums[l]<=target<nums[mid]:
                    r=mid
                elif nums[mid]<target<=nums[r]:
                    l=mid+1
                else:
                    return mid
            return l
