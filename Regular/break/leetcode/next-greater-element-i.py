class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hashMap = {n: i for i,n in enumerate(nums1)}

        res = [-1] * len(nums1)
        stack = []
        for j in range(len(nums2)):
            cur = nums2[j]
            while stack and stack[-1] < cur:
                val = stack.pop()
                indx = hashMap[val]
                res[indx] = cur
            if cur in hashMap:
                stack.append(cur)
        return res