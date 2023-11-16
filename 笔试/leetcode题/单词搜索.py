class Solution:
    def exist(self, board, word):
        m = len(board)
        n = len(board[0])

        def dfs(x, y, k):
            if not 0 <= x < m or not 0 <= y < n or board[x][y] != word[k]:
                return False
            elif k == len(word) - 1:
                return True
            else:
                board[x][y] = ''
                res = dfs(x + 1, y, k + 1) or dfs(x - 1, y, k + 1) or dfs(x, y + 1, k + 1) or dfs(x, y - 1, k + 1)
                board[x][y] = word[k]
            return res

        for i in range(m):
            for j in range(n):
                if dfs(i, j, 0):
                    return True
        return False
