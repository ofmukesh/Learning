class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        ans=0
        # count row servers
        for row in range(len(grid)):
            firstServerIdx=None
            countServers=0
            for col in range(len(grid[row])):
                if grid[row][col]==1:
                    grid[row][col]=-1
                    countServers+=1
                    if firstServerIdx==None:
                        firstServerIdx=col
            if countServers==1:
                grid[row][firstServerIdx]=1
            else:
                ans+=countServers
        
        # count column servers
        for col in range(len(grid[0])):
            countServers=0
            countServers2=0
            for row in range(len(grid)):
                if grid[row][col]==1:
                    countServers+=1
                if grid[row][col]==-1:
                    countServers2+=1
            if countServers2+countServers>1:
                ans+=countServers
        return ans
