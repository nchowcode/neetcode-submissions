# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # a valid path sum includes no stops
        # it is root, root.left, root.right
        # if we decide to skip a node, ie it is a negative, compare it to global val, and identify if that leads to lower total val... but what if the negative path leads to a higher value node all together??
        # my intutition seem smore like dp

        result = float("-inf")

        def dfs(node):
            nonlocal result

            if not node:
                return 0

            # capture gains of left and right
            leftGain = max(0, dfs(node.left))
            rightGain = max(0, dfs(node.right))

            # compare curr result, with total gain, only account for boosts, max(0,path)
            # anyways since it is building bottom up, we capture it all.
            result = max(result, node.val + leftGain + rightGain)

            # we have to pick the path that is greater
            return node.val + max(leftGain, rightGain)
        
        dfs(root)

        return result