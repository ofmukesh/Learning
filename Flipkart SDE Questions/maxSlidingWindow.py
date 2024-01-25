from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        output = []

        for idx, n in enumerate(nums):
            # getting rid of the idx that are outdated for our new window 
            while q and q[0] < idx - k + 1:
                q.popleft()
            
            # popping out numbers that are smaller than current num n from the right of the q 
            while q and n > nums[q[-1]]:
                q.pop()

            q.append(idx)

            # start logging answers after you have reached the desired window size of 'k'
            if idx >= k-1:
                output.append(nums[q[0]])

        return output 
