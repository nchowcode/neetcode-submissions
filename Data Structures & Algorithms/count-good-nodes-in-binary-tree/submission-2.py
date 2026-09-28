# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # dfs, track local max, + 1, update max if encountered.
        # run dfs from root, return total count

        def dfs(node, maxN) -> int:
            if not node:
                return 0
            
            if node.val >= maxN:
                left = dfs(node.left, node.val)
                right = dfs(node.right, node.val)
                return 1 + (left + right)
            else:
                left = dfs(node.left, maxN)
                right = dfs(node.right, maxN)
                return left + right

        

        return dfs(root, root.val)



            