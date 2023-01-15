import numpy as np
class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        t=[[0] * n for _ in range(n)]
        arr=np.array(t);
        for q in queries:
            r1=q[0]
            r2=q[2]
            c1=q[1]
            c2=q[3]
            arr[r1:r2+1,c1:c2+1]+=1
        return arr
