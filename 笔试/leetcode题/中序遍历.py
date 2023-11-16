class Solution:
    def inorderTraversal(self, root) :
        array = []
        if root is None:
            return []
        else:
            array.append(root.val)
            self.inorderTraversal(root.left, array)
            self.inorderTraversal(root.right, array)
        return array