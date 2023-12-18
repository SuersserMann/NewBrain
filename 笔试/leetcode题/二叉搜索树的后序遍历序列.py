#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param sequence int整型一维数组
# @return bool布尔型
#
class Solution:
    def VerifySquenceOfBST(self, sequence):
        if not sequence:
            return False

        def dfs(left, right):
            if left < right:
                for i in range(left, right):
                    if sequence[i] > sequence[right]:
                        b = i
                        for j in range(b, right):
                            if sequence[j] <= sequence[right]:
                                return False
                        c = dfs(left, b - 1)
                        d = dfs(b, right - 1)
                        return c and d
                return True
            else:
                return True

        return dfs(0, len(sequence) - 1)


solution = Solution()
result = solution.VerifySquenceOfBST([4, 6, 7, 5])
print(result)
