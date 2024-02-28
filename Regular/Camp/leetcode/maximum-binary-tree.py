# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:

        def formBinary(nums):
            if len(nums) > 0:
                lrg = max(nums)
                indx = nums.index(lrg)
                root = TreeNode(lrg)
                root.left = formBinary(nums[0:indx]) if indx > 0 else None
                root.right = formBinary(nums[indx + 1:]) if indx < len(nums) else None
            else:
                return None
            return root
        return formBinary(nums)
        