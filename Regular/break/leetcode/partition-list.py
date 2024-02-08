# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        left,right = ListNode(),ListNode()

        lft,rght = left,right

        while head:
            if head.val < x:
                lft.next = head
                lft = lft.next
            else:
                rght.next = head
                rght = rght.next
            head = head.next
        lft.next = right.next
        rght.next = None
        return left.next