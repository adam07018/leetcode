from collections import deque
class Solution:
    def findBottomLeftValue(self, root) -> int:
        if not root:
            return 0
        # bfs
        q = deque()
        q.append(root)
        left = root.val
        while q:
            size = len(q)
            flag = True
            while (size > 0):
                node = q.popleft()
                if flag:
                    left = node.val
                    flag = False
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                size -= 1
        return left
            
            