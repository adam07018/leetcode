class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root: return 
        while root:
            if root.val > q.val and root.val > p.val:
                root = root.left
            elif root.val < q.val and root.val < p.val:
                root = root.right 
            else:
                return root