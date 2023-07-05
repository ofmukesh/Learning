def find(nums,target):
    l=0
    r=len(nums)-1
    while l<r:
        mid=int((l+r)/2)
        if nums[mid]==target:
            return mid
        elif nums[mid]<target:
            l=mid+1
        else:
            r=mid-1
    return l

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        idx=find(nums,target) # finding the index of target element 
        if idx<len(nums) and nums[idx]==target:
            start=idx
            while start-1>=0 and nums[start-1]==target:
                start-=1
            end=idx
            while end+1<len(nums) and nums[end+1]==target:
                end+=1
            return [start,end]
        else:
            return [-1,-1]
