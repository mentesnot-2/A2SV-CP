# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        val=[]
        curr=head
        tar=head
        while curr:
            val.append(curr.val)
            curr=curr.next
        return val==val[::-1]
        # i=0
        # while tar:
        #     if tar.val!=val[i]:
        #         return False
        #     tar=tar.next
        #     i+=1
        # return True