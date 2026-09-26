# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # brute force: rebuild list with another list to store ordering and then just reference each node there. (main tradeoff is space)
        # optimal: reverse and merge in place without another storage.

        # find the mid point, reverse the 2nd half, then go, L -> R -> L -> R and list will be built.
        
        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # now fast will have reached the end, slow would be located at midpoint now, right at the end of [1] <- [2]
        # [first] - [second]

        second = slow.next
        first = slow
        slow.next = None # seperate
        prev = None
        
        # 1->2->3
        # 1->None
        # 2->1
        # 3->2
        # reverse the second list.
        while second:
            temp = second.next # temp = 2
            second.next = prev # 1->None | prev node
            prev = second # prev = curr (1)
            second = temp # curr = 2 for next iter.

        # second = None. Prev is our point of last change.
        # prev is now the 3->2->1->None
        first = head
        second = prev

        # why while second? since is never gonna be longer than first
        # we need temp to store, since we are modifying orginal array.

        # don't think of it as building an array 1 by 1, think of it as moving pointers and interleaving.
        while second:
            temp1 = first.next
            temp2 = second.next

            first.next = second
            second.next = temp1

            first = temp1
            second = temp2


            


        
