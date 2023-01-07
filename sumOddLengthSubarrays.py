class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        s=0;
        for i in range(len(arr)):
            s+=int(((i+1)*(len(arr)-i)+1)/2)*arr[i];
        return s;
