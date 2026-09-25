# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # at every iter, we need to store curr and prev.
        # before burning the bridge for "next", we need to refer to the node first.

        prev = None
        curr = head

        # NULL -> Head -> Head.next?
        # NULL <- Head <-> Head.next
        while curr:
            # check next node first?
            nextNode = curr.next # could be none... but we are setting it up for while loop
            curr.next = prev
            prev = curr
            curr = nextNode

        # not curr, because curr could be a dummy next node with no references, as while loop breaks out.
        return prev

        
