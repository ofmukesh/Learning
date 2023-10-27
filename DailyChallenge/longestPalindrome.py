class Solution:
    def longestPalindrome(self, s: str) -> str:
        # Step 1: Preprocess the input string
        processed_str = "^#"
        for c in s:
            processed_str += c + "#"
        processed_str += "$"

        # Step 2: Initialize variables for the algorithm
        str_length = len(processed_str)
        palindrome_lengths = [0] * str_length
        center = 0  # Current center of the palindrome
        right_edge = 0  # Rightmost edge of the palindrome

        # Step 3: Loop through the modified string to find palindromes
        for i in range(1, str_length - 1):
            palindrome_lengths[i] = min(right_edge - i, palindrome_lengths[2 * center - i]) if right_edge > i else 0

            # Expand the palindrome around the current character
            while processed_str[i + 1 + palindrome_lengths[i]] == processed_str[i - 1 - palindrome_lengths[i]]:
                palindrome_lengths[i] += 1

            # Update the rightmost edge and center if necessary
            if i + palindrome_lengths[i] > right_edge:
                center = i
                right_edge = i + palindrome_lengths[i]

        # Step 4: Find the longest palindrome and its center
        max_length = 0
        max_center = 0
        for i in range(str_length):
            if palindrome_lengths[i] > max_length:
                max_length = palindrome_lengths[i]
                max_center = i

        # Step 5: Extract the longest palindrome from the modified string
        start = (max_center - max_length) // 2
        end = start + max_length

        # Return the longest palindrome in the original string
        return s[start:end]
