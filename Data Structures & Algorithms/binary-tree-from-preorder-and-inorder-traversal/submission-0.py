# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # Root Left Right
        # Left Root Right

        if not preorder or not inorder:
            return None

        print(preorder, inorder)
        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])
        preorder.pop(0)

        root.left = self.buildTree(preorder, inorder[:mid])
        root.right = self.buildTree(preorder, inorder[mid+1:])

        return root
        



        