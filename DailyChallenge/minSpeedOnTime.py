class Solution:
    def time_required(self,speed):
        time=0
        for d in self.list[:-1]:
            time+=(d+speed-1)//speed
        time+=self.list[-1]/speed
        return time

    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        self.list=dist
        left=1
        right=10**9
        min_speed=-1

        while left<=right:
            mid=(left+right)//2
            if self.time_required(mid) <= hour:
                min_speed=mid
                right=mid-1
            else:
                left=mid+1
        
        return min_speed
