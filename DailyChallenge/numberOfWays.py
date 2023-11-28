class Solution:
    def numberOfWays(self, corridor):
        x = 1 # 0 seat
        y = 0 # 1 seat
        z = 0 # 2 seats
        for char in corridor:
            if char == 'S':
                x, y, z = 0, x + z, y
            else:
                x, y, z = x + z, y, z
        return z % (10**9+7) 
