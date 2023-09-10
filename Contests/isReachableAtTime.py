class Solution:
    def abs_dist(self,a,b):
        if a-b < 0:
            return b-a
        return a-b
        
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        if sx == fx and sy == fy:
            if t == 1: return False
            
            return True
        
        d1=self.abs_dist(sx,fx)
        d2=self.abs_dist(sy,fy)
        
        max_d=max(d1,d2)
        
        if max_d <= t: return True
        
        return False
        
        
