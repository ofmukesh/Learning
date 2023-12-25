class Solution:
    def numDecodings(self, s):
        if s == "0":
            return 0

        dp = [0 for _ in s]
        dp.append(1)

        dp[-2] = int(s[-1] != "0")

        i = len(s) - 2
        while i >= 0:
            if s[i] == "0":
                dp[i] = 0
            else:
                dp[i] = dp[i + 1]
                if (s[i] == "1") or (s[i] == "2" and int(s[i + 1]) < 7):
                    dp[i] += dp[i + 2]
            i -= 1
        
        return dp[0]
