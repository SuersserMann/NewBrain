class Solution:
    # def exist(self, board, word):
    #     m = len(board)
    #     n = len(board[0])
    #
    #     def dfs(x, y, k):
    #         if not 0 <= x < m or not 0 <= y < n or board[x][y] != word[k]:
    #             return False
    #         elif k == len(word) - 1:
    #             return True
    #         else:
    #             board[x][y] = ''
    #             res = dfs(x + 1, y, k + 1) or dfs(x - 1, y, k + 1) or dfs(x, y + 1, k + 1) or dfs(x, y - 1, k + 1)
    #             board[x][y] = word[k]
    #         return res
    #
    #     for i in range(m):
    #         for j in range(n):
    #             if dfs(i, j, 0):
    #                 return True
    #     return False

    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(i, j, k):
            if not 0 <= i < len(board) or not 0 <= j < len(board[0]) or board[i][j] != word[k]: return False
            if k == len(word) - 1: return True
            board[i][j] = ''
            res = dfs(i + 1, j, k + 1) or dfs(i - 1, j, k + 1) or dfs(i, j + 1, k + 1) or dfs(i, j - 1, k + 1)
            board[i][j] = word[k]
            return res

        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i, j, 0): return True
        return False
