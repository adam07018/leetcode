class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findMode(self, root):
        maxCount = 0
        count = 0
        pre = None
        ans = []
        def dfs(node):
            if not node:
                return
            nonlocal maxCount
            nonlocal pre
            nonlocal count
            dfs(node.left)

            if not pre:
                count = 1
            else:
                if pre.val == node.val:
                    count += 1
                else:
                    count = 1
            pre = node

            if count == maxCount:
                ans.append(node.val)
            elif count > maxCount:
                maxCount = count
                ans.clear()
                ans.append(node.val)
            dfs(node.right)
            
        dfs(root)
        return ans

root = TreeNode(1)
root.right = TreeNode(2)
print(Solution.findMode(Solution,root))
            

