# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def Height(node):
            if node is None:
                return 0
            left_ht = Height(node.left)
            right_ht = Height(node.right)
            if left_ht < 0 or right_ht < 0 or abs(left_ht - right_ht) > 1:
                return -1
            return max(left_ht, right_ht) + 1
        height = Height(root)
        return height >= 0