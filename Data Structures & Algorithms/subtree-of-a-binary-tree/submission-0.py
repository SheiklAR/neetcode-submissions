# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if (root and not subRoot) or (not root and not subRoot):
            return True
        
        if not root and subRoot:
            return False
        
        q = deque([])
        q.append(root)

        def isSubRoot(node1, node2):
            q1 = deque([])
            q2 = deque([])

            q1.append(node1)
            q2.append(node2)

            while q1:
                for _ in range(len(q1)):
                    n1, n2  = q1.popleft(), q2.popleft()

                    # print(n1, n2)

                    if n1.val != n2.val: return False

                    if (n1.left is None) != (n2.left is None):
                        return False
                    if (n1.right is None) != (n2.right is None):
                        return False
                    
                    if n1.left:
                        q1.append(n1.left)
                        q2.append(n2.left)
                    if n1.right:
                        q1.append(n1.right)
                        q2.append(n2.right)


            return True


        while q:
            
            for _ in range(len(q)):
                node = q.popleft()

                if node.val == subRoot.val and isSubRoot(node, subRoot):
                    return True

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)


        return False

