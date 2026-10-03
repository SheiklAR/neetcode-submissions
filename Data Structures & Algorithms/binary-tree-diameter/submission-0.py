# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        # two possibilities
        # at current level right + left
        # the one we return max(right, left)

        ans = 1

        def dfs(node):
            if not node:
                return 0
            nonlocal ans

            left, right = dfs(node.left), dfs(node.right)

            print(left, right)
            ans = max(ans, 1 + left + right)
            return 1 + max(left, right)


        dfs(root)
        return ans - 1