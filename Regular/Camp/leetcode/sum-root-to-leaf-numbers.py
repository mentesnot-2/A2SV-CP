# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def pathSum(path,root):
            if not root:
                return 0
            path = path * 10 + root.val

            if not root.right and not root.left:
                return path
            return pathSum(path,root.left) + pathSum(path,root.right)
        return pathSum(0,root)