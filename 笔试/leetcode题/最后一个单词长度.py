class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        space=False
        res=0
        for i in range(len(s)-1,-1,-1):
            if s[i]!=' ':
                space = True
            if space and s[i]!=' ':
                res+=1
            if space and s[i]==' ':
                return res
        return res
s=Solution()
print(s.lengthOfLastWord("Hello World"))
