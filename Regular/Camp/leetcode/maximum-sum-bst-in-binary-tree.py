# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        self.ans = 0

        def mxSum(root):
            if not root:
                return True,float("inf"),float("-inf"),0
            left_is_bst,left_mn,left_mx,left_sm = mxSum(root.left)
            right_is_bst,right_mn,right_mx,right_sm = mxSum(root.right)

            if left_is_bst and right_is_bst and left_mx < root.val < right_mn:
                sub_tree_sum = left_sm + right_sm + root.val
                self.ans = max(self.ans,sub_tree_sum)
                return True,min(left_mn,root.val),max(right_mx,root.val),sub_tree_sum
            return False,float("inf"),float("-inf"),0
        mxSum(root)
        return self.ans 
        