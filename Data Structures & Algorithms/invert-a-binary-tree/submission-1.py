# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # essentially we are just adjusting the left and rights of each given node.

        if root:
            left = root.left
            right = root.right
            
            root.left = right
            root.right = left

            self.invertTree(left)
            self.invertTree(right)


        return root