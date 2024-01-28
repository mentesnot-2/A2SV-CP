class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        average = (sum(nums[:k]) ) / k
        mx_sum = sum(nums[:k])


        for i in range(k,len(nums)):
            mx_sum-=nums[i - k]
            mx_sum+=nums[i]
            avrg = (mx_sum)/ k  
            average = max(average,avrg)
        return average
            

        