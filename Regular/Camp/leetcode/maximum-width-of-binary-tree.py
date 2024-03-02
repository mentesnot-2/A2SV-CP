# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        queue = deque([(root,0)])
        ans = 0

        while queue:
            val = len(queue)
            curr = queue[-1][1] - queue[0][1] + 1
            while val:
                node,indx = queue.popleft()
                
                val-=1
                if node.left:
                    queue.append((node.left,2 * indx + 1))
                if node.right:
                    queue.append((node.right,2 * indx + 2))
            
            ans = max(ans,curr)
        return ans