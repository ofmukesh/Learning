class Solution:
    def getRightSum(self,customers,grumpy,window):
        s=0
        for idx,customer in enumerate(customers):
            if grumpy[idx]==0:
                s+=customer

        for i in range(window):
            if grumpy[i]==0:
                s-=customers[i]
        return s

    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        leftSum=0
        windowSum=sum(customers[0:minutes])
        rightSum=self.getRightSum(customers,grumpy,minutes)
        
        i,j=0,minutes-1
        ans=0
        while j<len(customers):
            try:
                ans=max(ans,leftSum+windowSum+rightSum)
                leftSum+=customers[i] if grumpy[i]==0 else 0
                rightSum-=customers[j+1] if grumpy[j+1]==0 else 0
                windowSum-=customers[i]
                windowSum+=customers[j+1]
                i+=1
                j+=1
            except:
                break
        
        return ans
