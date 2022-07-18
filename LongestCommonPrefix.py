class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        fs=strs[0]
        for i in range(len(strs)):
            temp=""
            for j in range(len(fs)):
                if j<len(strs[i]):
                    if strs[i][j]==fs[j]:
                        temp+=fs[j]
                    else:
                        fs=temp
                        break
                else:
                    fs=temp
                    break
            fs=temp
        return fs
