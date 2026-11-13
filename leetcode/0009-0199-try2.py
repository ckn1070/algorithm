# Solved - 어렵게..
# 아니 왜 처음 풀 때보다 훨씬 더 어려운 것 같지? 미치겠네..
# 아 Right부터 넣을 수가 있겠구나
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rightSideView(self, root: TreeNode | None) -> list[int]:

        q = deque()
        lv = 0
        q.append((root, lv))

        result = []
        while q:
            cur, depth = q.popleft()
            if cur is None:
                continue

            if not q or depth != q[0][1]:
                result.append(cur.val)
                lv += 1

            if cur.left is not None:
                q.append((cur.left, depth + 1))
            if cur.right is not None:
                q.append((cur.right, depth + 1))

        return result