class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def deleteNode(self, root, key: int) :
        if root == None:
            return root
        if root.val == key:
            # the return type is the new node (or null) to replace the deleted node
            if root.left == None and root.right == None:
                return None
            if root.left == None:
                return root.right
            if root.right == None:
                return root.left

            target = root.right
            while target.left:
                target = target.left
            target.left = root.left
            return root.right

        if key < root.val:
            root.left = self.deleteNode(Solution,root.left,key)
        else:
            root.right = self.deleteNode(Solution,root.right,key)
        return root

root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(6)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.right.right = TreeNode(7)
print(Solution.deleteNode(Solution,root,3))
        
        