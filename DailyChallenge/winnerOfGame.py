# Define a Python class named Solution
class Solution:
    
    # Define a method named winnerOfGame that takes a string 'colors' as input
    def winnerOfGame(self, colors: str) -> bool:
        
        # Create a counter object to count occurrences of characters
        c = collections.Counter()
        
        # Iterate through consecutive groups of identical characters
        for x, t in groupby(colors):

            # Calculate the number of consecutive characters and add it to the respective counter
            c[x] += max(len(list(t)) - 2, 0)
        
        # Check if the count of 'A' is greater than the count of 'B'
        if c['A'] > c['B']:
            return True  # 'A' wins, so return True
        return False  # 'B' wins or it's a tie, so return False
