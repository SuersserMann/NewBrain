class Solution:
    def findAnagrams(self, s: str, p: str):
        if len(s) < len(p):
            return []
        res = []
        s_list = [0] * 26
        p_list = [0] * 26

        for i in range(len(p)):
            s_list[ord(s[i]) - 97] += 1
            p_list[ord(p[i]) - 97] += 1
        if s_list == p_list:
            res.append(0)
        for i in range(len(s) - len(p)):
            s_list[ord(s[i]) - 97] -= 1
            s_list[ord(s[i + len(p)]) - 97] += 1
            if s_list == p_list:
                res.append(i + 1)
        return res
