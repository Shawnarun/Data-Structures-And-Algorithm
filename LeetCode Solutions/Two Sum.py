#https://leetcode.com/problems/two-sum/description/
class Solution:
    def twoSum(self, nums, x):
        reminder= {}
        for i in range(len(nums)):
            balance= x - nums[i]
            if balance in reminder:
                return [reminder[balance],i]
            else:
                reminder[nums[i]] = i
        return -1




nums = [2,7,11,15]
target = 9
#Output: [0,1]


solution = Solution()
print(solution.twoSum(nums, target))