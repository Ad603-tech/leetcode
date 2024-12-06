# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return root
        
        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        else:
            if not root.left and not root.right:
                return None
            if not root.left:
                return root.right
            if not root.right:
                return root.left
            
            pred = self.findMax(root.left)
            root.val = pred.val  # Replace value
            # Delete the inorder successor
            root.left = self.deleteNode(root.left, pred.val)

        return root

    def findMax(self, root):
        # Helper function to find the smallest value in the BST
        while root.right:
            root = root.right
        return root