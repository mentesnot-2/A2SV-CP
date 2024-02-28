# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:

        self.ans = 0
        def findSum(root,path,sofar):
            if not root:
                return 0
            path+=root.val
            
            if path - targetSum in sofar:
                self.ans+=sofar[path - targetSum]
           
            if path not in sofar:
                sofar[path] = 0
            sofar[path]+=1
            
            findSum(root.left,path,sofar.copy())
            findSum(root.right,path,sofar.copy())
        findSum(root,0,{0:1})
        return self.ans
        