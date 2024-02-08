# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        srt = []
        cur = head
        while cur:
            srt.append(cur.val)
            cur = cur.next

        srtd = sorted(srt)

        dummy = ListNode()
        tail = dummy
        for i in srtd:
            tail.next = ListNode(i)
            tail = tail.next
        tail.next = None
        return dummy.next
        