# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # preorder = NLR
        # inorder = LNR

        # desired output is the height tree left to right.
        
        if not preorder or not inorder:
            return None

        preorderIndex = 0
        inorderIndex = {value:index for index,value in enumerate(inorder)}

        def build(left, right):
            nonlocal preorderIndex

            if left > right:
                return None

            rootValue = preorder[preorderIndex]
            preorderIndex += 1

            root = TreeNode(rootValue)
            middle = inorderIndex[rootValue]

            root.left = build(left, middle - 1)
            root.right = build(middle + 1, right)

            return root

        return build(0, len(inorder) - 1)

            
