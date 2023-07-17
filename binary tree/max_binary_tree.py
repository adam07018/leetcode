class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def constructMaximumBinaryTree(self, nums: list[int]) :
        if len(nums) == 0:
            return None
        max = nums[0]
        if len(nums) == 1:
            return TreeNode(max)
        index = 0
        for i in range(len(nums)):
            if nums[i] > max:
                max = nums[i]
                index = i
        root = TreeNode(max)
        root.left = self.constructMaximumBinaryTree(nums[:index])
        if index < len(nums) - 1:
            root.right = self.constructMaximumBinaryTree(nums[index + 1:])
        return root

nums = [3,2,1,6,0,5]
print(Solution.constructMaximumBinaryTree(Solution,nums))