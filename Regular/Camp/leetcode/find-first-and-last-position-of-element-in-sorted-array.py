class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        def first(nums,target,n):
            l,r = 0,n - 1
            res = -1

            while l <= r:
                mid = l + (r - l) // 2

                if nums[mid] > target:
                    r = mid - 1
                elif nums[mid] < target:
                    l = mid + 1

                else:
                    res = mid
                    r = mid - 1
            return res
        def last(nums,target,n):
            l,r = 0,n - 1
            res = -1

            while l <= r:
                mid = l + (r - l) // 2

                if nums[mid] > target:
                    r = mid - 1
                elif nums[mid] < target:
                    l = mid + 1

                else:
                    res = mid
                    l = mid + 1
            return res
        return (first(nums,target,n),last(nums,target,n))
            
