class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.nums=sorted(nums)
        self.k=k

    def add(self, val: int) -> int:
        f=False
        for i in range(len(self.nums)):
            if self.nums[i] >= val:
                self.nums.insert(i,val)
                f=True
                break
        if not f:
            self.nums.append(val)
            
        return self.nums[len(self.nums)-self.k]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
