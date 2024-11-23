'''
# My algo is little bit different bcz gravity works first then the box is rotated :)

so on every row we just store the blank cells and the replace them with stones,
while iterating each cell of box, we will follow some rules:
    1. if any obstacle will come then we will clean the stored cells
    2. if the current cell is stone then we will replace it with the first blank cell and set blank to the current 
    cell, and also we need to remove blank cell from stored cells and append the new one
    3. id the current cell is empty we will simply store that

after the gravity works we simply convert the box matrix row into columns and columns into row
'''
class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        # in my world the gravity work first
        for row in range(len(box)):
            availablBlanks=[]
            for col in range(len(box[row])-1,-1,-1):
                curr=box[row][col]
                if curr==".":
                    # add the blank col to the list
                    availablBlanks.append(col)
                elif curr=="*":
                    # pop all elements from blankList:availablBlanks
                    while availablBlanks:
                        availablBlanks.pop()
                else:
                    # if we have blanks
                    if availablBlanks:
                        # replace the last blank with stone
                        box[row][availablBlanks[0]]="#" 
                        # set current col to blank
                        box[row][col]="."
                        availablBlanks.pop(0)
                        availablBlanks.append(col)

        # then I rotate the matrix 90 degree
        ans=[[] for _ in box[0]]
        for row in range(len(box)):
            for col in range(len(box[row])-1,-1,-1):
                ans[col].insert(0,box[row][col])
        return ans
