class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:

        # def get_next(index,current):
        #     return (current+nums[index])%len(nums)

        for index in range(len(nums)):
            slow,fast = index,index

            sign = 1 if nums[index]>0 else -1
            # print('index',index,'\n')
            while sign*nums[fast]>0 and sign*nums[((nums[fast]+fast)%len(nums))]>0:
                slow=(nums[slow]+slow)%len(nums)
                temp = ((nums[fast]+fast)%len(nums))
                fast= (nums[temp]+temp)%len(nums)
                print(slow,fast,)
                # print(sign*nums[fast]>0 ,sign*nums[nums[fast]]>0)
                if(slow==fast):
                    # print(abs(nums[slow])%len(nums),len(nums))
                    if(abs(nums[slow])%len(nums)==0):
                        break
                    return True

        return False

        