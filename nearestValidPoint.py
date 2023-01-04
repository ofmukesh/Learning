class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        ans=-1;
        temp=100000;
        for i in range(len(points)):
            if x==points[i][0] or y==points[i][1]:
                cal=abs(x-points[i][0])+abs(y-points[i][1]);
                print(cal)
                if cal<temp:
                    temp=cal;
                    ans=i;
        return ans;
