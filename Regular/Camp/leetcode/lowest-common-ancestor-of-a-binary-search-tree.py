# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        now=root
        while now:
            if p.val>now.val and q.val>now.val:
                now=now.right
            elif p.val<now.val and q.val<now.val:
                now=now.left
            else:
                return now