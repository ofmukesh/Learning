class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        prev=intervals[0]
        c=0
        for s,e in intervals[1:]:
            if s>=prev[1]:
                prev=[s,e]
            else:
                c+=1
                prev[1]=min(prev[1],e)
            
        return c
        
