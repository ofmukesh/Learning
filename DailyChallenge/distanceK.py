from collections import deque

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        if not root or not target:
            return []
        if k==0:
            return [target.val]
        
        parent={root: None}
        def dfs(root):
            if not root:
                return
            if root.left:
                parent[root.left]=root
                dfs(root.left)
            if root.right:
                parent[root.right]=root
                dfs(root.right)
        dfs(root)

        def bfs(root, level, visited):
            if not root or level<0:
                return []
            if root in visited:
                return []
            pool=deque()
            pool.append(root)
            visited.add(root)
            cnt=0
            while pool and cnt<level:
                tp=deque()
                while pool:
                    cur=pool.popleft()
                    if cur.left and cur.left not in visited:
                        tp.append(cur.left)
                        visited.add(cur.left)
                    if cur.right and cur.right not in visited:
                        tp.append(cur.right)
                        visited.add(cur.right)
                pool=tp
                cnt+=1
            ans=[]
            while pool:
                cur=pool.popleft()
                ans.append(cur.val)
            return ans
        
        tp=target
        ans=[]
        visited=set()
        for l in range(k+1):
            ans.extend(bfs(tp, k-l, visited))
            tp=parent[tp]
            if not tp:
                break
        return ans
