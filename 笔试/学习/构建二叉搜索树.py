# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        def build(left, right):  # 构建树的函数
            if left > right:  # 终止条件
                return None
            mid = (left + right)/2  # 中间值得下标
            root = TreeNode(nums[mid])  # 构建根节点
            root.left = build(left, mid - 1)  # 构建左子树
            root.right = build(mid + 1, right)  # 构建右子树
            return root  # 返回根节点
        res = build(0, len(nums) - 1)  # 调用函数
        return res