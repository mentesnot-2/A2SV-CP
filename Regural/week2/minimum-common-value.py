class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        n,m = len(nums1),len(nums2)
        first_ptr,scnd_ptr = 0, 0

        while first_ptr < n and scnd_ptr < m:
            if nums1[first_ptr] < nums2[scnd_ptr]:
                first_ptr+=1
            elif nums1[first_ptr] > nums2[scnd_ptr]:
                scnd_ptr+=1
            else:
                return nums1[first_ptr]
        if first_ptr < n:
            while first_ptr < n:
                if nums1[first_ptr] < nums2[scnd_ptr - 1]:
                    first_ptr+=1
                elif nums1[first_ptr] > nums2[scnd_ptr - 1]:
                    break
                else:
                    return nums1[first_ptr]
        if scnd_ptr < m:
            while scnd_ptr < m:
                if nums2[scnd_ptr] < nums1[first_ptr - 1]:
                    scnd_ptr+=1
                elif nums1[first_ptr - 1] < nums2[scnd_ptr - 1]:
                    break
                else:
                    return nums2[scnd_ptr]
            
        return -1