# Given the root of a binary tree, return all root-to-leaf paths in any order.
class Solution:
    def binaryTreePaths(self, root) -> list[str]:
        if not root:
            return []
        ans = []

        def backtrace(path, node):
            if not node.left and not node.right:
                path += str(node.val)
                ans.append(path)
                return
            #path += str(node.val) + "->"
            if node.left:
                backtrace(path + str(node.val) + "->", node.left)
            if node.right:
                backtrace(path + str(node.val) + "->", node.right)
        
        backtrace("", root)
        return ans
                
            