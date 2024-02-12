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
            if curr and curr.val in num:
                while curr and curr.val in num:
                    curr = curr.next
                count+=1
            if curr and curr.val not in num:
                curr = curr.next
                continue
        return count
        