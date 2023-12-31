class Solution:
    def letterCombinations(self, digits):
        dic = {"2": ['a', 'b', 'c'],
               "3": ['d', 'e', 'f'],
               "4": ['g', 'h', 'i'],
               "5": ['j', 'k', 'l'],
               "6": ['m', 'n', 'o'],
               "7": ['p', 'q', 'r', 's'],
               "8": ['t', 'u', 'v'],
               "9": ['w', 'x', 'y', 'z'],
               }
        n = len(digits)
        res = []
        if n==0:
            return res
        def back(path, deep):
            if deep == n:
                res.append(''.join(path))
                return
            for i in dic[digits[deep]]:
                path.append(i)
                back(path, deep + 1)
                path.pop()

        back([],0)
        return res