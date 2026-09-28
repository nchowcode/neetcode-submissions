# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # textbook BFS
        # QUEUE, append to list?
        # each item in queue from l->r appends new to queue after job execute?
        if not root:
            return []

        res = []
        queue = deque([root]) #start with root

        while queue:
            levelSize = len(queue)
            level = []
            for _ in range(levelSize):
                node = queue.popleft()
                level.append(node.val)

                left = node.left if node.left else None
                right = node.right if node.right else None
                
                if left:
                    queue.append(left)
                if right:
                    queue.append(right)
            res.append(level)
        
        return res





