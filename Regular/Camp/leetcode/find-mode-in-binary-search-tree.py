# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        

        def helper(root,mp):
            if not root:
                return mp
            mp[root.val]+=1
            helper(root.left,mp)
            helper(root.right,mp)
            return mp

        val = helper(root,defaultdict(int))
        print(val)
        mx = max(val.values())
        ans = []
        for i in val:
            if val[i] == mx:
                ans.append(i)
        return ans