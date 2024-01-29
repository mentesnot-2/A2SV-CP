class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        leftProd = [0] * len(nums)
        
        rightProd = [0] * len(nums)
        
        rightProd[len(nums) - 1] = 1
        
        leftProd[0] = 1
        
        for j in range(1, len(nums)):
            leftProd[j] = leftProd[j - 1] * nums[j - 1]
            
        for k in range(len(nums) - 2, -1, -1):
            rightProd[k] = rightProd[k + 1] * nums[k + 1]
            
            
        return [ rightProd[i] * leftProd[i] for i in range(len(nums))]
        