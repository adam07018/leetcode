# You are given an integer array nums. You are initially positioned at the array's first index, 
# and each element in the array represents your maximum jump length at that position.
# Return true if you can reach the last index, or false otherwise.
# https://leetcode.cn/problems/jump-game
class Solution:
    def canJump(self, nums: list[int]) -> bool:
        n = len(nums)
        if n == 1:
            return True
        far = nums[0]
        for i in range(n):
            if nums[i] == 0 and far == i:
                return False
            if far < nums[i] + i:
                far = nums[i] + i
            if far >= n - 1:
                return True
        return False

nums = [3,2,1,0,4]
print(Solution.canJump(Solution,nums))
