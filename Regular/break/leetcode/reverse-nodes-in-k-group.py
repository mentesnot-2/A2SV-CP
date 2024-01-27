# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        lst = []

        while head:
            lst.append(head.val)
            head = head.next
        i = 0
        while i < len(lst):
            if len(lst[i:i+k]) != k:
                i = i + k
                continue
            lst[i:i + k] = lst[i:i+k][::-1]
            i = i + k
        dummy = ListNode()
        curr = dummy
        for i in range(len(lst)):
            cur = ListNode(lst[i])
            curr.next = cur
            curr = curr.next

        return dummy.next
        