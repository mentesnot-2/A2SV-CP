# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        self.head = head
        # temp = current = head
        # length = 0
        # while temp is not None:
        #     temp = temp.next
        #     length+=1
        # if length == n:
        #     head = current.next
        # target = 0
        # temp = head
        # while temp:
        #     target+=1
        #     if (length-target) == n:
        #         temp.next = temp.next.next
        #     else:
        #         temp = temp.next

        dummy = ListNode(0,self.head)
        fast = dummy
        while n:
            fast = fast.next
            n-=1
        slow = dummy
        while fast.next:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        return dummy.next