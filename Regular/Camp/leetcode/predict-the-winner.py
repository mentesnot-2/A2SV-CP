class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:

        dp = {}

        def rec(left, right, p1turn):

            if (left, right, p1turn) in dp:
                return dp[(left, right, p1turn)]

            if left == right:
                if p1turn:
                    return nums[left]
                return 0
            if p1turn:
                pos1 = nums[left] + rec(left+1, right, False)
                pos2 = nums[right] + rec(left, right-1, False)
                dp[(left, right, p1turn)] = max(pos1, pos2)
                return dp[(left, right, p1turn)]
            else:
                pos1 = rec(left+1, right, True)
                pos2 = rec(left, right-1, True)
                dp[(left, right, p1turn)] = min(pos1, pos2)
                return dp[(left, right, p1turn)]

        p1Score = rec(0, len(nums)-1, True)

        return p1Score >= sum(nums)-p1Score