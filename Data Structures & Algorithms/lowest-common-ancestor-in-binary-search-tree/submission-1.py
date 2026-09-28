# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # how to store the min? ik at some point we need to do min(root) depending if we bottom up or top down.

        # if we do like a bottom up, we propogate a boolean that contains both...
        # seems like a greedy approach.

        # rules: BST, guranteed answer. tree node is always <= max(p,q)
        # tie breaker, 3,4 vs 5 3,4


        curr = root

        while curr:
            # both bigger
            if p.val > curr.val and q.val > curr.val:
                curr = curr.right
            # both smaller
            elif p.val < curr.val and q.val < curr.val:
                curr = curr.left
            # wincase = either node is = to target, or its the split.
            else:
                return curr
            
            

            # both smaller
