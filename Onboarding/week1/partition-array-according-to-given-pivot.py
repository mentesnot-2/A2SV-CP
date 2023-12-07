class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        pvt = []
        less = []
        grtr = []

        for i in nums:
            if i < pivot:
                less.append(i)
            elif i > pivot:
                grtr.append(i)
            else:
                pvt.append(i)

        return less + pvt + grtr