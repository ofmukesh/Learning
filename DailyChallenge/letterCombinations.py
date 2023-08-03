
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        KEY_MAP={'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        res=[]
        l=len(digits)

        if l==0:
            return res
        elif l==1:
            res=[c for c in KEY_MAP[digits[0]]]
        else:
            def backtrack(i,curr):
                if len(curr)==len(digits):
                    res.append(curr)
                    return
                for c in KEY_MAP[digits[i]]:
                    backtrack(i+1,curr+c)
            if digits:
                backtrack(0,'')
        return res



