class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        freq=Counter(nums2)
        intersection=[]
        for j in nums1:
           if freq[j]>0:
               intersection.append(j)
               freq[j]-=1
        return intersection