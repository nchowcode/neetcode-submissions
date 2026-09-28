# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # its basically the rightmost value at its level.
        # think of it like bfs, and if each is stored as a list, its level[-1]

        if not root:
            return []
        
        queue = deque([root])
        res = []

        while queue:
            # add to 
            level = []
            levelLength = len(queue)

            for _ in range(levelLength):
                node = queue.popleft()
                level.append(node.val)

                left = node.left if node.left else None
                right = node.right if node.right else None

                if left:
                    queue.append(left)
                if right:
                    queue.append(right)
            # print(queue)
            # print(level)
            rightSide = level[-1]
            res.append(rightSide)
        
        return res
