class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ans=[]
        l=len(nums)
        i=0
        while i<l:
            curr_ans=str(nums[i])
            isNxt=False
            while i+1<l and nums[i]+1==nums[i+1]:
                isNxt=True
                i+=1
            
            if isNxt:
                curr_ans+="->"+str(nums[i])
            ans.append(curr_ans)
            i+=1

        return ans
