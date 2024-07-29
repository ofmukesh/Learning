class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        greatest=max(candies)

        for i in range(len(candies)):
            candies[i] = True if candies[i]+extraCandies >= greatest else False
        
        return candies
