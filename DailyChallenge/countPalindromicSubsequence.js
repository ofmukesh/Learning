class Solution:
    def countPalindromicSubsequence(self, inputString):
        # Arrays to store the minimum and maximum occurrences of each character in the input string
        min_exist = [float('inf')] * 26
        max_exist = [float('-inf')] * 26

        # Populate min_exist and max_exist arrays
        for i in range(len(inputString)):
            char_index = ord(inputString[i]) - ord('a')
            min_exist[char_index] = min(min_exist[char_index], i)
            max_exist[char_index] = max(max_exist[char_index], i)

        # Variable to store the final count of unique palindromic subsequences
        unique_count = 0

        # Iterate over each character in the alphabet
        for char_index in range(26):
            # Check if the character has occurred in the input string
            if min_exist[char_index] == float('inf') or max_exist[char_index] == float('-inf'):
                continue  # No occurrences, move to the next character

            # Set to store unique characters between the minimum and maximum occurrences
            unique_chars_between = set()

            # Iterate over the characters between the minimum and maximum occurrences
            for j in range(min_exist[char_index] + 1, max_exist[char_index]):
                unique_chars_between.add(inputString[j])

            # Add the count of unique characters between the occurrences to the final count
            unique_count += len(unique_chars_between)

        # Return the total count of unique palindromic subsequences
        return unique_count
