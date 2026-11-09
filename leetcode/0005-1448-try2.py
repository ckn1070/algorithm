# Solved
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0

        def dfs(nodes, cur):
            nonlocal count
            if nodes is None:
                return

            if nodes.val >= cur:
                count += 1

            cur = max(nodes.val, cur)
            dfs(nodes.right, cur)
            dfs(nodes.left, cur)

        dfs(root, -10 ** 18)
        return count

