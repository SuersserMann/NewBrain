class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        dp = [[[0] for _ in range(len(nums)+1)] for _ in range(len(nums))+1]
        z=len(nums)
        for i in range(1,z):
            for j in range(1,z):

