class Solution:
    def numIslands(self, grid) -> int:
        if not grid:
            return 0
        m = len(grid)
        n = len(grid[0])
        res = 0

        def dfs(x, y):
            if x >= m or x < 0 or y >= n or y < 0:
                return
            if grid[x][y] != '1':
                return
            grid[x][y] = '2'
            if x < m:
                dfs(x + 1, y)
            if x > 0:
                dfs(x - 1, y)
            if y < n:
                dfs(x, y + 1)
            if y > 0:
                dfs(x, y - 1)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    dfs(i, j)
                    res += 1
        return res


grid = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
]
s = Solution()
print(s.numIslands(grid))
