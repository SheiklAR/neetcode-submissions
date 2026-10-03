# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        

        def dfs(node):
            if not node:
                return (0,0)
            
            left, right = dfs(node.left), dfs(node.right)
            print(node.val + left[1] + right[1], left[0] + right[0])

            return (
                node.val + left[1] + right[1],
                max(left[0] + right[0], left[0] + right[1], left[1] + right[0], right[1] + left[1])
            )


        return max(dfs(root))

