class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        res=1
        for i in range(len(points)):
            point1=points[i]
            count=collections.defaultdict(int)
            for j in range(i+1,len(points)):
                point2=points[j]
                if point1[0]==point2[0]:
                    slope=float('inf')
                else:
                    slope=(point2[1]-point1[1])/(point2[0]-point1[0])
                count[slope]+=1
                res=max(res,count[slope]+1)
        return res
