# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        q1 = deque([])
        q2 = deque([])

        if p and q:
            q1.append(p)
            q2.append(q)
        else:
            if not p and not q:
                return True
            else:
                return False
        
        while q1:
            n = len(q1)

            for _ in range(len(q1)):
                node1, node2 = q1.popleft(), q2.popleft()

                if not (node1.val == node2.val): return False


                if not ((node1.left and node2.left) or  (not node1.left and not node2.left)):
                    return False
                if not ((node1.right and node2.right) or (not node1.right and not node2.right)):
                    return False
                
                if node1.left:
                    q1.append(node1.left)
                    q2.append(node2.left)
                if node1.right:
                    q1.append(node1.right)
                    q2.append(node2.right)

                
            
            
        return True