class Solution:
    def isPalindrome(self, x: int) -> bool:
        x=str(x)
        n=len(x)
        left = 0
        right = n - 1
        while left <= right and x[left] == x[right]:
            if left == right:
                return True
            elif left+1==right:
                return True
            left += 1
            right -= 1
        else:
            return False