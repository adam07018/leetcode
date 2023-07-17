class Solution:
    def fourSum(self, nums, target):
        # 同 3sum
        n = len(nums)
        nums.sort()
        ans = []
        for i in range(n):
            # 剪枝, target can be neagative
            if (nums[i] > target and nums[i] >= 0): #todo
                break
            # 去重
            if (i > 0 and nums[i] == nums[i - 1]):
                continue
            for j in range(i + 1, n):
                # 剪枝
                if (nums[i] + nums[j] > target and nums[i] + nums[j] >= 0): #todo
                    break
                #去重
                if (j > i + 1 and nums[j] == nums[j - 1]):
                    continue
                left = j + 1
                right = n - 1
                while left < right:
                    sum = nums[i] + nums[j] + nums[left] + nums[right]
                    if sum < target:
                        left += 1
                    elif sum > target:
                        right -= 1
                    else:
                        ans.append([nums[i],nums[j],nums[left],nums[right]])
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1
                        left += 1
                        right -= 1
        return ans
