class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0
        points.sort()
        prev=points[0]
        c=1
        for s,e in points[1:]:
            if s>prev[1]:
                c+=1
                prev=[s,e]
            else:
                prev[1]=min(prev[1],e)
            
        return c
        
