# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.ans = []

        def traverse(root,row,col):
            if not root:
                return
            self.ans.append((row,col,root.val))
            traverse(root.left,row + 1,col - 1)
            traverse(root.right,row + 1,col  +1)
        traverse(root,0,0)
        self.ans.sort(key=lambda x :(x[1],x[0],x[2]))
        prev_col = float("-inf")
        result = []
        for row,col,val in self.ans:
            if col != prev_col:
                prev_col = col
                result.append([])
            result[-1].append(val)
        return result
