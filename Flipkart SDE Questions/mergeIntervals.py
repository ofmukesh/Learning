class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        merged=[intervals[0]]
        for curr in intervals[1:]:
            if curr[1]<merged[-1][1]:
                continue
            elif curr[0]<=merged[-1][1]:
                merged[-1][1]=curr[1]
            else:
                merged.append(curr)
        return merged
