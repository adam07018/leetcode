from collections import deque
class Solution:
    def levelOrder(self, root) -> list[list[int]]:
        list = []
        path = []
        q = deque()
        q.append(root)
        while q:
            size = len(q)
            while (size > 0):
                node = q.popleft()
                if node:
                    path.append(node.val)
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
                size -= 1
            list.append(path.copy())
            path.clear()
        return list

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
#root.left.left = TreeNode(4)
#root.left.right = TreeNode(5)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
print(Solution.levelOrder(Solution, root))