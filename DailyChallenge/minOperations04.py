# store frequency of numbers, then minimize and calculate operations
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        # frequency counting
        frq={}
        for num in nums:
            frq[num]=frq.get(num,0)+1
        print(frq)
        # count operations 
        oprts=0
        for key in frq.keys():
            # if the frquency is 1 then there is no possible ways to make array empty so, return -1
            if frq[key]==1:
                return -1 
            else:
                # if frq[key]%3 != 0, so we have to add 1 extra operation because imagine num%3=1 or 2, 
                # so we delete elements 3,3,... but 1 or 2 is remaining so 1 extra operation should be needed     
                if frq[key]%3!=0:
                    oprts+=frq[key]//3+1
                # if frq[key]%3 == 0 so, we can delete the current element like 3,3,...  
                else:
                    oprts+=frq[key]//3

        return oprts
        # time complexity -> O(n)
        # space complexity -> O(n)
