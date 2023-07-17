class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, inorder: list[int], postorder: list[int]) -> TreeNode:
        if len(postorder) == 0:
            return None
        root = TreeNode(postorder[-1])
        if len(postorder) == 1:
            return root
        # find the index of root node in inorder
        index = -1
        for i in range(len(inorder)):
            if inorder[i] == root.val:
                index = i
        # cut inorder tree
        leftTree_in = inorder[:index]
        rightTree_in = inorder[index + 1:]
        # cut postorder tree
        leftTree_post= postorder[:index]
        rightTree_post = postorder[index:len(postorder) - 1]
        root.left = self.buildTree(leftTree_in, leftTree_post)
        root.right = self.buildTree(rightTree_in, rightTree_post)
        return root