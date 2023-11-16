class Solution:
    def wordBreak(self, s: str, wordDict) -> bool:
        n=len(s)
        dp = [False] * (n+ 1)
        dp[0]=True
        for i in range(n):
            for j in range(i+1,n+1):
                if dp[i] and s[i:j] in wordDict:
                    dp[j]=True

        return dp[-1]

        # word = wordDict.copy()
        #
        # def dfs(path, word):
        #     if path.replace(' ', '') == '':
        #         return True
        #     if not word:
        #         return False
        #     m = len(word)
        #     for g in range(m):
        #         if word[g] in path:
        #             x = path.replace(word[g], ' ')
        #             c = word.copy()
        #             c.remove(word[g])
        #             if dfs(x, c):
        #                 return True
        #     return False
        #
        # return dfs(s, word)


s = Solution()
print(s.wordBreak("ddadddbdddadd", ["dd", "ad", "da", "b"]))
