# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root, targetSum):

        def dfs(node, target):
            if not node:
                return 0
            if node.val == target:
                ans = 1
            else:
                ans = 0
            return ans + dfs(node.left, target - node.val) + dfs(node.right,target - node.val)

        if not root:
            return 0
        return dfs(root, targetSum) + self.pathSum(root.left, targetSum) + self.pathSum(root.right, targetSum)


root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(-3)
root.left.left = TreeNode(3)
root.left.right = TreeNode(2)
root.right.right = TreeNode(11)
root.left.left.left = TreeNode(3)
root.left.left.right = TreeNode(-2)
root.left.right.right = TreeNode(1)
s = Solution()

# 测试 pathSum 函数
target_sum = 8
result = s.pathSum(root, target_sum)

# 打印结果
print(result)
