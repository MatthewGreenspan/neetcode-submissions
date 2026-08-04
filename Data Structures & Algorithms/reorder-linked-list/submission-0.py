# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # find middle using floyds cycle detection, slow is middle
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # cut off second half from first, save slow.next and subsequent nodes to second
        # sever the connection by setting slow.next = None
        second = slow.next
        slow.next = None

        # set current = to the new starting point of the second half
        prev, curr = None, second
        # reversal
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        # head = [0,1,2,3], prev = [6,5,4]
        while prev:

            savedHead = head.next       # [1, 2, 3]
            savedPrev = prev.next       # [5, 4]

            head.next = prev            #
            prev.next = savedHead

            head = savedHead
            prev = savedPrev





            
            