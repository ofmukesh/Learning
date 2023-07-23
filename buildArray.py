# Solution 1:- T.C O(n) & S.C O(n)
class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        ans=[]
        for i in range(len(nums)):
            ans.append(nums[nums[i]])
        
        return ans


# Solution 1:- T.C O(n) & S.C O(1)
class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i in range(0, n):
            nums[i] = n * ( nums[nums[i]] % n) + nums[i]
        for i in range(0,n):
            nums[i] = nums[i] // n
        return nums
