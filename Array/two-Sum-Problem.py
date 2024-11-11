class Solution:

    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[j] == target - nums[i]:
                    return[i, j]
        return []
    
nums = [1,5,6,9,7,2,4,3]
target = 11
target1 = 16
target2 = 15
target3 = 10

s1 = Solution()
print(s1.twoSum(nums,target))
print(s1.twoSum(nums,target1))
print(s1.twoSum(nums,target2))
print(s1.twoSum(nums,target3))
    
