# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current=head
        targ=set()
        while current:
            if current in targ:
                return current
            targ.add(current)
            current=current.next
        return None