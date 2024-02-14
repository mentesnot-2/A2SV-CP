class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        moves = 0

        while maxDoubles and target > 1:
            moves+=((target % 2) + 1)
            maxDoubles-=1
            target = target // 2
        moves+=(target -1)
        return moves

        