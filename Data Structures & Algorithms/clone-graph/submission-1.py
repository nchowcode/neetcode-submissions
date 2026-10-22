"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import deque
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # node index is same as its value.
        # ik we must use dfs to traverse neighbors and list the node's neighbors
        if not node:
            return node
        # example flow:
        # start at 1. the neighboring list is listed in the neighbors field, we need to create new nodes that map to it.
        # deep copy means that it shares the same neighbors, has the same value, but is a new Node object.
        # now we begin with its neighbors.
        
        # original : copy
        copies = {}
        
        def dfs(originalNode):
            # check if node exists
            if not originalNode:
                return

            if originalNode in copies:
                return copies[originalNode]
            
            copyNode = Node(originalNode.val)
            copies[originalNode] = copyNode

            # neighbors added shortly.            
            for originalNeighbor in originalNode.neighbors:
                copiedNeighbor = dfs(originalNeighbor)
                copyNode.neighbors.append(copiedNeighbor)

            return copyNode

        root = dfs(node)
        return root



