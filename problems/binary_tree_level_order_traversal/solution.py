# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque()
        result = []
        q.append(root)

        while q:
            qlen = len(q)
            val_list = []
            for i in range(qlen):
                curr = q.popleft()
                if curr:
                    val_list.append(curr.val)
                    q.append(curr.left)
                    q.append(curr.right)
                
            if val_list:
                result.append(val_list)
        return result