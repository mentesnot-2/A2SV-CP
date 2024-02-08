# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy=ListNode()
        tail=dummy
        cur1=head
        tar=[]
        while cur1:
            tar.append(cur1.val)
            cur1=cur1.next
        tar[(left-1):right]=tar[(left-1):(right)][::-1]
        for i in tar:
            tail.next=ListNode(i)
            tail=tail.next
        return dummy.next
               
        