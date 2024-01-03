class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        ans=0
        lastCount=0
        
        for i in range(len(bank)-1,-1,-1):
            currCount=0
            for char in bank[i]:
                if char=="1":
                    currCount+=1
            if lastCount!=0 and currCount!=0:
                ans+=(lastCount*currCount)
            
            if currCount!=0:
                lastCount=currCount
        return ans

        # Time complexity -> O(n*m), n is the length of array bank and m is the max length of bank elements
        # Space complexity -> O(1)
