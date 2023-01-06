class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:

        x=coordinates[1][0]-coordinates[0][0]
        y=coordinates[1][1]-coordinates[0][1]

        for i in range(2,len(coordinates)):
            xd=coordinates[i][0]-coordinates[i-1][0]
            yd=coordinates[i][1]-coordinates[i-1][1]
            if xd*y != yd*x:
                return False
        return True
      
      
