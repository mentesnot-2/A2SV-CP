# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        self.ans = 0
        def total(root):
            if not root:return 0
            if low <= root.val<=high:
                self.ans+=root.val
                total(root.left)
                total(root.right)
            elif root.val < low:
                total(root.right)
            elif root.val > high:
                total(root.left)
            
        total(root)
        return self.ans

        