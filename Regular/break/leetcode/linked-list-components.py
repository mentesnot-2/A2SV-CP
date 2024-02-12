# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:
        num = set(nums)
        curr = head
        count = 0
        while curr:
            if curr.val in num and not(curr.next and curr.next.val in num):
                count+=1
            curr = curr.next
        return count
        