class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        nums.sort()
        tmp={}
        ans=-1
        for num in nums:
            tmp[num]=1
        
        for num in nums:
            curr=num
            l=1
            while curr**2 in tmp:
                l+=1
                curr=curr**2

            if l>=2 and l>ans:
                ans=l

        return ans
