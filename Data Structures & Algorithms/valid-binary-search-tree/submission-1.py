# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # 1. all nodes left of node must be smaller
        # 2. all nodes right of node must be larger

        # if left, we must pass in 2, check that its < 2.
        # if right, we must pass in 2, check its > 2

        # but... how do we differentiate left and right logic in dfs?
        # if you think about it, rightside has to be greater than min < curr < max
        # leftside, is simply min < curr < max
        def dfs(node, localmin, localmax):
            if not node:
                return True

            if not (localmin < node.val < localmax):
                return False
            
            # left = setting new max
            # right = setting new min
            left = dfs(node.left, localmin, node.val)
            right = dfs(node.right, node.val, localmax)
            return left and right
        

        return dfs(root,float("-inf"),float("inf"))
            
            