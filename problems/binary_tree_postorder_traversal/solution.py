# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []

        def posttravel(node):
            if not node:
                return
            posttravel(node.left)
            posttravel(node.right)
            result.append(node.val)
        
        posttravel(root)
        return result
        