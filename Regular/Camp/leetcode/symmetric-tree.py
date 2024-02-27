# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        return self.mirror(root.left,root.right)
    def mirror(self,leftroot,rightroot):
        if leftroot and rightroot: 
            return leftroot.val==rightroot.val and self.mirror(leftroot.left,rightroot.right) and self.mirror(leftroot.right,rightroot.left)
        return leftroot==rightroot