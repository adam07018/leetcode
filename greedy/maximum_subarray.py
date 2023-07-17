class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        max = nums[0]
        sum = 0
        for i in nums:
            sum += i
            if max < sum:
                max = sum
            if sum < 0:
                sum = 0
        return max

