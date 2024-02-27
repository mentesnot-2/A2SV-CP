# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        self.ans = float("-inf")
        def ancestor(root, minval, maxval):
            if root:
                minval = min(minval, root.val)
                maxval = max(maxval, root.val)
                self.ans = max(self.ans, maxval - minval)
                ancestor(root.left, minval, maxval)
                ancestor(root.right, minval, maxval)
            
        ancestor(root, root.val, root.val)
        return self.ans
        