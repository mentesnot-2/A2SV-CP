# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        stack = deque([root])
        dfs = []
        if not root:return []
        depth = 0
        while stack:
            depth+=1
            val = len(stack)
            ans = []
            while val:
                curr = stack.popleft()
                ans.append(curr.val)
                val-=1
                if curr.left:stack.append(curr.left)
                if curr.right:stack.append(curr.right)
            if depth % 2 == 0:
                ans = ans[::-1]
            dfs.append(ans)
        # bfs()
        return dfs

                