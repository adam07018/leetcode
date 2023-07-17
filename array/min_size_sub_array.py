def minSubArrayLen(target, nums):
    i, j = 0,0
    min = len(nums) + 1
    sum = nums[0]
    while i < len(nums) and j < len(nums):
        if sum >= target: # left side of window move right
            if j - i + 1 < min: # if current window length is minimum
                min = j - i + 1
            sum -= nums[i]
            i += 1
        else: 
            j += 1
            if j < len(nums):
                sum += nums[j]
    if min == len(nums) + 1:
        return 0
    return min

nums = [2,3,1,2,4,3]
print(minSubArrayLen(7,nums))