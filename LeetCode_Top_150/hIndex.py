class Solution:
    def hIndex(self, citations: List[int]) -> int:
        arr=[0 for _ in range(len(citations)+1)]

        for c in citations:
            if c < len(arr):
                arr[c]+=1
            else:
                arr[-1]+=1
        
        c=0
        for i in range(len(arr)-1,-1,-1):
            c+=arr[i]
            if c>=i:
                return i
        return 0
