# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        nodes = []

        def treverse(root):
            if not root:return
            nodes.append(root.val)
            treverse(root.left)
            treverse(root.right)

        treverse(root)

        print(nodes)