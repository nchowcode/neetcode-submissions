# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root: # means theres subroot still
            return False
        
        if self.sameTree(root, subRoot):
            return True
        
        # otherwise we explore next options, left and right.
        return (self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot))

    def sameTree(self, node, subroot) -> bool:
        # think of all the possible cases
        # 1. root ends, subroot doesn't end - return false
        # 2. both ends, - return true
        # 3. both match, keep traversing

        if not node and not subroot:
            return True
        
        if not node or not subroot or node.val != subroot.val:
            return False

        if node.val == subroot.val:
            left = self.sameTree(node.left, subroot.left)
            right = self.sameTree(node.right, subroot.right)

            return left and right
        
        # assuming theyre not equal
        return False



