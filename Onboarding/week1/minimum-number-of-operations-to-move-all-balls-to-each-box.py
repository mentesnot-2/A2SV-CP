class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        mp = {i:boxes[i] for i in range(len(boxes))}
        ans = []
        for i in range(len(boxes)):
            cnt = 0
            for j in mp:
                if j != i and mp[j] == "1":
                    cnt+=abs(j-i)
            ans.append(cnt)
        return ans


        