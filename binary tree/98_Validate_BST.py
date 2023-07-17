class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root) -> bool:
        pre = None
        def dfs(root):
            nonlocal pre
            if not root:
                return True
            if not dfs(root.left):
                return False
            if not pre:
                pre = root
            else:
                if pre.val >= root.val:
                    return False
                else:
                    pre = root
            if not dfs(root.right):
                return False
            return True
        return dfs(root)

root = TreeNode(1)
root.left = TreeNode(1)
print(Solution.isValidBST(Solution,root))
