class Solution:
    def reconstructQueue(self, people):
        nums = (sorted(people, key=lambda x: (-x[0], x[1]), reverse=True))
        res = []
        for i in range(len(nums)):
            if nums[i][1] == nums.index(nums[i]):
                res.append(nums[i])
            else:
                res.insert(nums[i][1], nums[i])
        return res
