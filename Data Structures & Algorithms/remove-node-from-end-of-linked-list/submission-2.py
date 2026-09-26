# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # init counter
        # store prev and make prev.next = curr.next.
        # return head.

        counter = 0

        dummy = ListNode(0,head)
        curr = head

        while curr:
            counter += 1
            curr = curr.next
        
        target = counter - n # target idx
        curr = head
        prev = dummy

        # logging prev and curr.
        for _ in range(target):
            prev = curr
            curr = curr.next

        # on the curren target. We want to skip over it 2->3->4 = 2->->4
        prev.next = curr.next

        return dummy.next