class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        totalTimeToRemove=0
        i=0
        while i<len(colors):
            currSum=neededTime[i]
            currMax=neededTime[i]
            while i+1<len(colors) and colors[i]==colors[i+1]:
                currMax=max(currMax,neededTime[i+1])
                currSum+=neededTime[i+1]
                i+=1
            totalTimeToRemove+=currSum-currMax
            i+=1
            
        return totalTimeToRemove
