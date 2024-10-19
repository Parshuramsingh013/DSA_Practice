class Solution:
    def missingNumber(self, nums):
        N = len(nums)
        sum =  (N*(N+1))//2

        sum2 =  0
        for i in range(N):
            sum2 += nums[i]
        return sum - sum2


nums = [2,3,4,6,5,7]   
s1 = Solution()
print(s1.missingNumber(nums))