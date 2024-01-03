class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        slow_pointer,fast_pointer = 0,0
        n = len(nums)

        while fast_pointer < n :
            if nums[slow_pointer] == nums[fast_pointer]:

                fast_pointer+=1
            else:
                 nums[slow_pointer + 1] = nums[fast_pointer]
                 slow_pointer+=1
            # print(nums)
        return slow_pointer + 1

        