# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque()
        result = []
        q.append(root)
        left_to_right = True

        while q:
            size = len(q)
            val_list = []

            for i in range(size):
                curr = q.popleft()
                if curr:
                    val_list.append(curr.val)
                    if curr.left:
                        q.append(curr.left)
                    if curr.right:
                        q.append(curr.right)
            if not left_to_right:
                val_list.reverse()

            if val_list:
                result.append(val_list)
                left_to_right = not left_to_right

        return result