# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        ln,cur = 0,head
        while cur:
            ln+=1
            cur = cur.next
            
        cur = head
        res = []
        
        bs,rm = ln // k, ln % k
        
        for i in range(k):
            res.append(cur)
            
            for j in range(bs - 1 + (1 if rm else 0)):
                if not cur: break
                cur = cur.next
            rm-= (1 if rm else 0)
            if cur:
                temp = cur.next
                cur.next = None
                cur = temp
                # cur.next,cur = None,cur.next
        return res