"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # create copy node 
        # for each copy, need: og next, og random (and create copy of it.)
        # we can map it, create a reference for each copied node.

        # pre processing to build the hashmap new : old

        # post processing to apply pointers to each



        copyMap = {None:None}
        curr = head

        while curr:
            newNode = Node(curr.val)
            copyMap[curr] = newNode
            curr = curr.next
        

        # print(copyMap)

        curr = head
        
        while curr:
            # access copy
            copyNode = copyMap[curr]
            copyNode.next = copyMap[curr.next]
            copyNode.random = copyMap[curr.random]

            curr = curr.next

        return copyMap[head]

        





