class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode:
        if len(preorder) == 0:
            return None
        root = TreeNode(preorder[0])
        if len(preorder) == 1:
            return root
        # find root in inorder
        index = -1
        for i in range(len(inorder)):
            if inorder[i] == root.val:
                index = i
        # slice inorder list
        left_in = inorder[0:index]
        right_in = inorder[index + 1:]
        # slice preorder list
        left_pre = preorder[1: index + 1]
        right_pre = preorder[index + 1:]
        
        root.left = self.buildTree(left_pre,left_in)
        root.right = self.buildTree(right_pre, right_in)
        return root