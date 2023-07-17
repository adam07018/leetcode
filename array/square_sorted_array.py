def sortedSquares(nums):
    array = [0] * len(nums)
    index = len(nums) - 1
    i = 0
    j = len(nums) - 1
    while i <= j:
        if nums[i] < 0:
            if nums[i] ** 2 > nums[j] ** 2:
                array[index] = nums[i] ** 2
                i += 1
            else:
                array[index] = nums[j] ** 2
                j -= 1
        else:
            array[index] = nums[j] ** 2
            j -= 1
        index -= 1
    return array

nums = [-4,-1,0,3,10]
print(sortedSquares(nums))
    


