class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        freq=Counter(nums)
        for j in freq:
            if freq[j]>1:
                return True
                break
        return False