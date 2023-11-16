class Solution:
    def countBits(self, n: int) -> List[int]:
        return [bin(i) for i in range(1,n+1)]