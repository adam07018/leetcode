class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedArrayToBST(self, nums) :
        n = len(nums)
        if n == 0:
            return None
        if n == 1:
            return nums[0]
        mid = int(n / 2)
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(Solution,nums[0:mid])
        root.right = self.sortedArrayToBST(Solution,nums[mid + 1:])
        return root

nums = [1,2,3,5]
root = Solution.sortedArrayToBST(Solution,nums)
print('yes')