# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # it feels like a propagating right -> node -> right
        # maybe have a running counter of k - curr?

        # need to go all the way left first
        res = []

        def dfs(node):
            if not node:
                return
            left = node.left
            right = node.right
            # always store curr, left, right
            dfs(left)
            res.append(node.val)
            dfs(right)
        
        dfs(root)

        return res[k - 1]
        





            