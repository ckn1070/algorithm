# Solved
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def leafSimilar(self, root1: TreeNode | None, root2: TreeNode | None) -> bool:
        leaf1 = []
        leaf2 = []

        def dfs(nodes, leaves):
            if nodes is None:
                return

            if nodes.left is None and nodes.right is None:
                leaves.append(nodes.val)
                return

            dfs(nodes.left, leaves)
            dfs(nodes.right, leaves)

        dfs(root1, leaf1)
        dfs(root2, leaf2)

        return leaf1 == leaf2
