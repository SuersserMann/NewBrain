# Definition for a binary tree node.
from collections import deque


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ' '
        res = []
        queue = deque([root])

        while queue:
            node = queue.popleft()
            if node:
                res.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else:
                res.append("null")

        return ",".join(res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if data == ' ':
            return []
        res = data.split(',')
        queue = deque(res)
        root = TreeNode(int(queue[0]))
        stack = deque([root])
        queue.popleft()
        while stack:
            node = stack.popleft()
            if queue:
                x = queue.popleft()
                if x != 'null':
                    left = TreeNode(int(x))
                    node.left = left
                    stack.append(left)

            if queue:
                y = queue.popleft()
                if y != 'null':
                    right = TreeNode(int(y))
                    node.right = right
                    stack.append(right)

        return root


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)

# 构建二叉树结构
node1.left = node2
node1.right = node3
node3.left = node4
node3.right = node5

# 返回根节点

s = Codec()

a = s.serialize(node1)
print(a)
b = s.deserialize(a)
cc = deque([b])

while cc:
    ff = cc.popleft()
    print(ff.val)
    if ff.left:
        cc.append(ff.left)
    if ff.right:
        cc.append(ff.right)
