class Solution:
    def insert_spaces(self, line, words_amount, space_difference):
        if words_amount == 1:
            line[0] = line[0].ljust(space_difference+len(line[0]))
            return

        spaces = space_difference // (words_amount - 1)
        spaces_remainder = space_difference % (words_amount - 1)

        for index in range(words_amount - 1):
            if index < spaces_remainder:
                line[index] += ' ' * (spaces + 1)
            else:
                line[index] += ' ' * spaces

    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
            length, cur_line, result = 0, [], []
            
            for word in words:
                words_amount = len(cur_line)
                if length + len(word) + words_amount > maxWidth:
                    space_difference = maxWidth - length

                    self.insert_spaces(cur_line, words_amount, space_difference)
                
                    result.append(''.join(cur_line))
                    
                    length = 0
                    cur_line = []
                
                cur_line.append(word)
                length += len(word)
                
            last_line = ' '.join(cur_line).ljust(maxWidth)
            result.append(last_line)
            return result
        
        
        # result = full_justify(words, maxWidth)
        # print(result)
