class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        n = len(nums)
        last = nums[n - 1]  # Initialize 'last' with the last element
        ans = 0  # Initialize the total operations count

        # Traverse the array in reverse order
        for i in range(n - 2, -1, -1):
            if nums[i] > last:  # If the current element needs replacement
                t = nums[i] // last  # Calculate how many times the element needs to be divided
                if nums[i] % last:
                    t += 1  # If there's a remainder, increment 't'
                last = nums[i] // t  # Update 'last' for the next comparison
                ans += t - 1  # Add (t - 1) to 'ans' for the number of operations
            else:
                last = nums[i]  # Update 'last' without replacement
        return ans  # Return the total number of operations
