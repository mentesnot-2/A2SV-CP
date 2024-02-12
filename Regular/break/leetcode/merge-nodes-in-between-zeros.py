# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        curr = dummy
        curr_sum = 0
        current = head.next
        while current and current.next:
            curr_sum+=current.val
            if current.next.val == 0:
                curr.next = ListNode(curr_sum)
                curr = curr.next
                current = current.next.next
                curr_sum = 0
            else:
                current = current.next
        return dummy.next
        