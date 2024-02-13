# Definition for singly-linked list.
# class ListNode:
#     def init(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        dirn = 'r'
        matrix = [[-1]*n for _ in range(m)]
        i = 0
        j = 0
        curr = head
        while curr:

            matrix[i][j] = curr.val

            if dirn=='r':
                if j+1 >= n or matrix[i][j+1]!=-1:
                    dirn = 'd'
                    i += 1
                else:
                    j += 1

            elif dirn=='l':
                if j-1 < 0 or matrix[i][j-1]!=-1:
                    dirn = 'u'
                    i -= 1
                else:
                    j -= 1
                
            elif dirn=='u':
                if i-1 < 0 or matrix[i-1][j]!=-1:
                    dirn = 'r'
                    j += 1
                else:
                    i -= 1

            elif dirn=='d':
                if i+1 >= m or matrix[i+1][j]!=-1:
                    dirn = 'l'
                    j -= 1
                else:
                    i += 1

            curr = curr.next
        return matrix