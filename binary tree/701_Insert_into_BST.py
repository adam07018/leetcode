class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def insertIntoBST(self, root, val: int) :
        pre = None
        cur = root
        left = -1
        while cur:
            pre = cur
            if cur.val > val:
                cur = cur.left
                left = 1
            else:
                cur = cur.right
                left = 0
        node = TreeNode(val)
        if left == -1:
            return node
        if left == 1:
            pre.left = node
        else:
            pre.right = node
        return root
        
            
        

        