class Solution:
    def searchMatrix(self, matrix, target: int) -> bool:
        if not matrix:
            return False
        m = len(matrix)
        n = len(matrix[0])
        i, j = m - 1, 0
        while i > 0 and j < n - 1:
            if matrix[i][j] > target:
                i -= 1
            elif target > matrix[i][j]:
                j += 1
            else:
                return True
        return False
