# Solved
#
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def pathSum(self, root: TreeNode | None, targetSum: int) -> int:
        answer = 0

        def acc(nodes, before):
            nonlocal answer
            if nodes is None:
                return

            after = before + nodes.val
            if after == targetSum:
                answer += 1

            acc(nodes.left, after)
            acc(nodes.right, after)

        def dfs(nodes):
            if nodes is None:
                return

            acc(nodes, 0)

            dfs(nodes.left)
            dfs(nodes.right)

        dfs(root)
        return answer