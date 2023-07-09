class Solution:
    def largestVariance(self, s: str) -> int:
        freq1 = 0
        freq2 = 0
        variance = 0
        
        # create distinct list of character pairs
        pairs = [(l1, l2) for l1 in set(s) for l2 in set(s) if l1 != l2]

        # run once for original string order, then again for reverse string order
        for runs in range(2):
            for pair in pairs:

                for letter in s:
                    # no reason to process letters that aren't part of the current pair
                    if letter not in pair:
                        continue
                    if letter == pair[0]:
                        freq1 += 1
                    elif letter == pair[1]:
                        freq2 += 1
                    if freq1 < freq2:
                        freq1 = freq2 = 0
                    elif freq1 > 0 and freq2 > 0:
                        variance = max(variance, freq1-freq2)
                freq1 = freq2 = 0
            
            # reverse the string for the second time around
            s = s[::-1]
                
        return variance
