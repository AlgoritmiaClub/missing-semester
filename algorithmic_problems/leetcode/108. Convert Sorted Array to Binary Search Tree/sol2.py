# Definition for a binary tree node (LeetCode).
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

####################################################

#Iterative with Queue Solution

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None

        n = len(nums)
        mid = (0 + n - 1) // 2
        root = TreeNode(nums[mid])

        q = deque()
        if 0 <= mid - 1:
            q.append((root, 0, mid - 1, True))
        if mid + 1 <= n - 1:
            q.append((root, mid + 1, n - 1, False))

        while q:
            parent, l, r, is_left = q.popleft()
            m = (l + r) // 2
            node = TreeNode(nums[m])

            if is_left:
                parent.left = node
            else:
                parent.right = node

            if l <= m - 1:
                q.append((node, l, m - 1, True))
            if m + 1 <= r:
                q.append((node, m + 1, r, False))

        return root
