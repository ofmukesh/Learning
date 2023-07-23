class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        result = []
        for word in words:
            # Split the word by the separator and exclude empty strings
            split_words = [w for w in word.split(separator) if w != '']
            result.extend(split_words)
        return result
