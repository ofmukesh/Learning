class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        appears=len(arr)//4
        result=0
        i=0
        while i<len(arr):
            tmp=1
            result=arr[i]
            while i+1<len(arr) and arr[i]==arr[i+1]:
                tmp+=1
                i+=1
            if tmp>appears:
                break
            i+=1
        return result
