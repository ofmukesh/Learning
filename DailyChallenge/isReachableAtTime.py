class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        
        if(sy==fy and sx==fx and t==1):
            return 0;
        t_x = abs(fx-sx)
        t_y = abs(fy-sy)
        x = t_x-t_y
        if x<=0:
            return t_y<=t
        else:
            return t_y+x<=t
