class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points.sort()
        diff = 0
        for i in range(1, len(points)):
            diff = max(diff, points[i][0] - points[i - 1][0])
        return diff

