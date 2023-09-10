class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        nums.sort()
        stck=[nums[0]]
        for s,e in nums[1:]:
            if stck[-1][1]>=s:
                stck[-1][1]=max(stck[-1][1],e)
            else:
                stck.append([s,e])
        ans=0
        for s,e in stck:
            ans+=e-s+1
        
        return ans
