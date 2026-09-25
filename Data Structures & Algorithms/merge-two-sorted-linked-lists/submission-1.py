# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = ListNode()
        node = dummy

        # at any stage of the iteration, we will consume the smallest possible. <= condition to consume.

        while list1 and list2:
            if list1.val < list2.val:
                node.next = list1
                list1 = list1.next
            else:
                node.next = list2
                list2 = list2.next
        
            node = node.next # we need to shift the pointer to next...

        # at this point, one will be done, remainder will just need to be added on in sorted order.

        node.next = list1 or list2 # whichever exists...

        return dummy.next