# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        nums = []
        def inorder(root):
            if not root:
                return 
            inorder(root.left)
            nums.append(root.val)
            inorder(root.right)
        inorder(root)

        def build(l,r):
            if l > r:
                return
            mid = (l  + r) // 2
            return TreeNode(nums[mid],build(l,mid - 1),build(mid + 1,r))
        l,r = 0,len(nums) - 1
        return build(l,r)