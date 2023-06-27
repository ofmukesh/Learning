class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        i=0
        while i<len(intervals) and intervals[i][0]<newInterval[0]:
            i+=1
        intervals.insert(i,newInterval)

        ans=[]
        for intrvl in intervals:
            if not ans or ans[-1][1]<intrvl[0]:
                ans.append(intrvl)
            else:
                ans[-1][1] = max(ans[-1][1], intrvl[1])

        return ans
