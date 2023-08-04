class Solution:
    def myAtoi(self, s: str) -> int:
        num_s=""
        t=['-','+',"0",'1','2','3','4','5','6','7','8',"9"]
        for i in range(len(s)):
            if s[i] in t:
                num_s+=s[i]
                if i+1<len(s) and (s[i+1] not in t or s[i+1]=="+" or s[i+1]=="-"):
                    break
            elif s[i]!=' ':
                return 0

        if num_s=="-" or num_s=="+" or num_s[:2]=="+-" or num_s[:2]=="-+" or num_s=="": return 0

        num=int(num_s)
        if num > (2**31)-1:
            return (2**31)-1
        elif num < -2**31:
            return (-2**31)
        else:
            return num
