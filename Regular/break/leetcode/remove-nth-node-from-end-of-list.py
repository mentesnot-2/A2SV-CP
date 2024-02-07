# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp=current=head
        length=0
        while temp is not None:
            temp=temp.next
            length+=1
        # if length==1:
        #     head=None
        if length==n:
            head=current.next
        target=0
        temp=head
        while temp:
            target+=1
            if (length-target)==n:
                temp.next=temp.next.next
            else:
                temp=temp.next
        return head