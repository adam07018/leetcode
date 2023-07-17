class Solution:
    def preorderTraversal(self, root) -> list[int]:
        list = []
        def backtrace(root):
            if not root:
                return
            list.append(root.val)
            backtrace(root.left)
            backtrace(root.right)
        backtrace(root)
        return list

    def postorderTraversal(self, root) -> list[int]:
        list = []
        def backtrace(root):
            if not root:
                return 
            backtrace(root.left)
            backtrace(root.right)
            list.append(root.val)
        backtrace(root)
        return list

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)
print(Solution.postorderTraversal(Solution, root))