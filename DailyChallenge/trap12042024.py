class Solution:
    def trap(self, height: List[int]) -> int:
        leftMax=[]
        rightMax=[]
        m=0
        m2=0
        for i in range(len(height)):
            m=max(height[i],m)
            leftMax.append(m)

            m2=max(height[len(height)-1-i],m2)
            rightMax.insert(0,m2)

        ans=0
        for i in range(len(height)):
            ans+=min(leftMax[i],rightMax[i])-height[i]

        return ans
