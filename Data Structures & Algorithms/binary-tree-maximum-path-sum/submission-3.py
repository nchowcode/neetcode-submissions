# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # dfs, we need to cmp local best to global best
        result = float("-inf")

        # dfs calculates all paths
        # 1. updates global res with curr node PLUS left + right
        # 2. updates local best chain recursively

        def dfs(node):
            nonlocal result
            if not node:
                return 0

            leftGain = max(0, dfs(node.left))
            rightGain = max(0, dfs(node.right))

            # 1. including all values
            includingNode = node.val + leftGain + rightGain
            result = max(result, includingNode)

            # 2. only including best path, must include curr node + best path gain
            # note: will always be > including node, since this will be passed into it later call
            largestPath = node.val + max(leftGain, rightGain)
            return largestPath
        
        dfs(root)
        return result

        