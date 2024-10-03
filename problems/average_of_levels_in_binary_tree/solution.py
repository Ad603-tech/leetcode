# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        q = deque()
        result = []
        q.append(root)

        while q:
            size = len(q)
            val_list = []

            for i in range(size):
                curr = q.popleft()
                if curr:
                    val_list.append(curr.val)
                    q.append(curr.left)
                    q.append(curr.right)

            if val_list:
                avg = sum(val_list)/len(val_list)
                result.append(avg)

        return result

