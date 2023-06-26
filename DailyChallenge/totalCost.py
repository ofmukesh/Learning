class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        q=costs[:candidates]
        r=costs[max(candidates,len(costs)-candidates):]
        heapify(q)
        heapify(r)
        res=0
        i=candidates
        j=len(costs)-candidates-1
        for _  in range(k):
            if not r or q and q[0]<=r[0]:
                res+=heappop(q)
                if i<=j:
                    heappush(q,costs[i])
                    i+=1

            else:
                res+=heappop(r)
                if i<=j:
                    heappush(r,costs[j])
                    j-=1
        
        return res
