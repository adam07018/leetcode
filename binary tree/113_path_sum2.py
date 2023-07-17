class Solution:
    def pathSum(self, root, targetSum: int):
        path = []
        ans = []
        def backtrace(node,targetSum):
            if not node:
                return
            path.append(node.val)
            if targetSum == node.val and not node.left and not node.right:
                ans.append(path.copy())
                path.pop()
                return
            targetSum -= node.val
            if node.left:
                backtrace(node.left,targetSum)
            if node.right:
                backtrace(node.right,targetSum)
            path.pop()
        backtrace(root,targetSum)
        return ans