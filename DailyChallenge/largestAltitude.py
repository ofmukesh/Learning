class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        highest=0
        curr_sum=0

        i=1
        while i<len(gain)+1:
            curr_sum=curr_sum+gain[i-1]
            highest=max(highest,curr_sum)
            i+=1

        return highest
