# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if not root:return
        stack = [root]
        dfs = []
        while stack:
            node = stack.pop()
            dfs.append(node.val)
            if node.left:stack.append(node.left)
            if node.right:stack.append(node.right)
        heapq.heapify(dfs)
        return heapq.nsmallest(k,dfs)[k - 1]