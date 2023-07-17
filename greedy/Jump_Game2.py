# Return the minimum number of jumps to reach nums[n - 1]
class Solution:
    def jump(self, nums: list[int]) -> int:
        n = len(nums)
        cur = 0
        next = 0
        result = 0
        for i in range(n):
            next = max(next, i + nums[i])
            if i == cur:
                if cur < n - 1:
                    result += 1
                    cur = next
                else:
                    return result
        return result
            
            

