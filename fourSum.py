class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        s = set()
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                l = j+1
                r = len(nums)-1
                while l<r:
                    if nums[i] + nums[j] + nums[l] + nums[r]<target:
                        l+=1
                    elif nums[i] + nums[j] + nums[l] + nums[r]>target:
                        r-=1
                    elif nums[i] + nums[j] + nums[l] + nums[r]==target:
                        s.add((nums[i],nums[j],nums[l],nums[r]))
                        l+=1
                        r-=1
        return list(s)
